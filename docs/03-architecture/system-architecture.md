# System Architecture

## 1. Sơ đồ tổng thể (high-level)

```
┌─────────────┐      HTTPS       ┌─────────────────────────────────┐
│   Frontend    │ ───────────────▶ │   Backend API (Python FastAPI)  │
│  (React/Vite)  │ ◀─────────────── │   /api/v1/...                   │
└─────────────┘                   └────────────────┬────────────────┘
                                                   │
              ┌────────────────────────────────────┼────────────────────────────┐
              │                                    │                            │
              ▼                                    ▼                            ▼
     ┌─────────────────┐                 ┌──────────────────┐        ┌──────────────────────┐
     │  PostgreSQL       │                 │   Redis Cache     │        │  AI Agent Module     │
     │  (SQLAlchemy/     │                 │  (session, API      │        │  (LangGraph Python)  │
     │   SQLModel)       │                 │   cache, rate-limit) │        │  trực tiếp trong app │
     │  users/events/    │                 └──────────────────┘        └──────────┬───────────┘
     │  plans/votes...   │                                                     │
     └─────────────────┘                                         ┌─────────────┴──────────┬───────────────┐
                                                                 ▼                        ▼               ▼
                                                       ┌──────────────────┐     ┌──────────────────┐    ┌───────────────┐
                                                       │ External APIs    │     │ DeepSeek API     │    │ Email/PDF     │
                                                       │ Google Places,   │     │ (V3 & R1)        │    │ Service (N5)  │
                                                       │ Mapbox, Weather  │     └──────────────────┘    └───────────────┘
                                                       └──────────────────┘
```

## 2. Nguyên tắc kiến trúc
- **Backend duy nhất (Python FastAPI)** — Tốc độ cao, hỗ trợ `async/await` native. Vì LangGraph cũng viết bằng Python, AI Agent và Backend API nằm cùng một mã nguồn Python (monorepo), không cần giao tiếp IPC/gRPC qua 2 ngôn ngữ khác nhau.
- **Hỗ trợ đa dạng EventType (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM)** — Backend FastAPI routers linh hoạt xử lý mọi loại sự kiện nhóm.
- **Nhóm 2 (Event/Plan/Vote) là nguồn sự thật duy nhất (single source of truth)** về dữ liệu sự kiện — AI Agent (Nhóm 4) thao tác dữ liệu thông qua SQLAlchemy Async Session layer của Nhóm 2.
- **Plan thủ công và Plan AI đối xử bình đẳng** — Cả hai đều lưu trạng thái `DRAFT`, đi qua luồng `VOTING`, và chỉ Owner mới `CONFIRMED`.
- **Nhóm 3 (External API) sử dụng `httpx` async và luôn đi qua lớp cache Redis** trước khi gọi ra ngoài — TTL đề xuất: địa điểm/nhà hàng 6–24h, thời tiết 1–3h, tỷ giá 12h.
- **AI Agent không có quyền ghi trực tiếp** vào DB những hành động ảnh hưởng người dùng khác (VD chốt plan cuối) mà không qua xác nhận/vote — xem `ai-agent-architecture.md` mục Human-in-the-loop.

## 3. Luồng dữ liệu chính (happy path)

### Luồng AI Hỗ Trợ Plan:
1. User A tạo Event (chọn EventType: `TRAVEL`, `DINING`, `ENTERTAINMENT`, ...) → mời thành viên qua email/link (`Invitation`).
2. Thành viên nhận notification → chấp nhận lời mời (`ACCEPTED`).
3. User yêu cầu AI đề xuất plan (Nhóm 4) → Orchestrator nhận `eventType`, phân loại intent bằng `deepseek-chat` → kích hoạt pipeline sub-agents phù hợp (Location, Research, Plan, Cost, Booking).
4. `deepseek-reasoner` hỗ trợ tối ưu lộ trình / gợi ý menu món ăn / phân giải xung đột.
5. AI trả về **Draft Plan** (`status = DRAFT`), hiển thị trực quan cho nhóm.
6. Người tạo gửi vote → `status = VOTING` → các thành viên vào vote (UP/DOWN/NEUTRAL) + comment.
7. Nếu vote phân tán → Conflict Resolver Agent đề xuất dung hòa.
8. Owner xác nhận (`CONFIRMED`) → Notification (N5) báo cho nhóm, sẵn sàng export PDF / nhắc nhở.

### Luồng Plan Thủ Công (Không Dùng AI):
1. Thành viên bấm **"Tạo plan mới"** trong Event → tự thêm từng điểm dừng (stop) bằng tay (hỗ trợ autocomplete từ Google Places API).
2. Lưu nháp (`status = DRAFT`, `isAiGenerated = false`).
3. Người tạo bấm **"Gửi vote"** → `status = VOTING` → cả nhóm vào vote & comment.
4. Owner xác nhận (`CONFIRMED`) → dùng chung đầy đủ các tính năng export PDF, xem bản đồ, chia chi phí.

## 4. Môi trường (Environments)
| Env | Mục đích | Domain |
|---|---|---|
| `local` | Máy dev cá nhân, Docker Compose | `localhost:8000` |
| `staging` | Test tích hợp trước release, dữ liệu giả | `staging.*` |
| `production` | Bản demo/nộp đồ án chính thức | domain chính |

## 5. Sơ đồ thư mục backend FastAPI đề xuất
```
travel-ai/
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── main.py           # FastAPI entrypoint, middlewares, CORS
│   │   ├── config.py         # Pydantic BaseSettings (.env loader)
│   │   ├── core/             # Security, JWT, DB session setup
│   │   │   ├── database.py   # SQLAlchemy async engine & session
│   │   │   └── security.py   # Password hashing & JWT tokens
│   │   ├── models/           # SQLAlchemy DB Models (User, Event, Plan, Vote...)
│   │   ├── schemas/          # Pydantic Schemas for Request/Response DTOs
│   │   ├── api/              # API Routers
│   │   │   ├── v1/
│   │   │   │   ├── auth.py
│   │   │   │   ├── events.py
│   │   │   │   ├── plans.py
│   │   │   │   ├── votes.py
│   │   │   │   ├── places.py
│   │   │   │   └── ai.py
│   │   ├── services/         # Business logic
│   │   └── ai_agents/        # LangGraph Multi-Agent system
│   │       ├── orchestrator.py
│   │       ├── agents/       # Location, Plan, Research, Conflict...
│   │       └── state.py      # LangGraph state schema
│   ├── alembic/              # Database migration scripts
│   ├── pyproject.toml        # Dependencies (Poetry / uv)
│   └── tests/                # Pytest unit & integration tests
├── frontend/                 # React Application
├── docs/                     # Tài liệu dự án
└── docker-compose.yml
```
