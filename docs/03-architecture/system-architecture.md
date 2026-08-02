# System Architecture

## 1. Sơ đồ tổng thể (high-level)

```
┌─────────────┐      HTTPS       ┌───────────────────────┐
│   Frontend    │ ───────────────▶ │   Backend API (NestJS)  │
│  (React/Vite)  │ ◀─────────────── │   /api/v1/...            │
└─────────────┘                   └───────────┬───────────┘
                                               │
              ┌────────────────────────────────┼────────────────────────────┐
              │                                │                            │
              ▼                                ▼                            ▼
     ┌─────────────────┐             ┌──────────────────┐        ┌──────────────────┐
     │  PostgreSQL       │             │   Redis Cache     │        │  AI Agent Module   │
     │  (Prisma ORM)      │             │  (session, API      │        │  (LangGraph)         │
     │  users/events/plans │             │   cache, rate-limit) │        │  → xem ai-agent-       │
     │  /votes/members/    │             └──────────────────┘        │     architecture.md   │
     │  invitations     │                                         └────────┬───────────┘
     └─────────────────┘                                              │
                                                                   ┌──┴────────┬────────────────┐
                                                                   ▼           ▼                ▼
                                                         ┌──────────────────┐┌───────────────┐┌───────────────┐
                                                         │ External APIs    ││ DeepSeek API  ││ Email/PDF     │
                                                         │ Google Places,   ││ (V3 & R1)     ││ Service (N5)  │
                                                         │ Mapbox, Weather  │└───────────────┘└───────────────┘
                                                         └──────────────────┘
```

## 2. Nguyên tắc kiến trúc
- **Backend duy nhất (monolith module hoá)** cho MVP — không tách microservice ngay từ đầu để tránh overhead vận hành không cần thiết cho quy mô đồ án. Có thể tách AI Agent thành service riêng (xem ADR nếu team quyết định).
- **Hỗ trợ đa dạng EventType (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM)** — Backend và AI Agent linh hoạt xử lý mọi loại sự kiện nhóm.
- **Nhóm 2 (Event/Plan/Vote) là nguồn sự thật duy nhất (single source of truth)** về dữ liệu sự kiện — AI Agent (Nhóm 4) đọc/ghi thông qua Service layer của Nhóm 2, không thao tác DB trực tiếp song song để tránh lệch dữ liệu.
- **Plan thủ công và Plan AI đối xử bình đẳng** — Cả hai đều lưu trạng thái `DRAFT`, đi qua luồng `VOTING`, và chỉ Owner mới `CONFIRMED`.
- **Nhóm 3 (External API) luôn đi qua lớp cache Redis** trước khi gọi ra ngoài — TTL đề xuất: địa điểm/nhà hàng/chỗ chơi 6–24h, thời tiết 1–3h, tỷ giá 12h.
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
| `local` | Máy dev cá nhân, Docker Compose | `localhost` |
| `staging` | Test tích hợp trước release, dữ liệu giả | `staging.*` |
| `production` | Bản demo/nộp đồ án chính thức | domain chính |

## 5. Sơ đồ thư mục monorepo đề xuất
```
travel-ai/
├── apps/
│   ├── backend/         # NestJS
│   ├── frontend/        # React
│   └── ai-service/       # (tuỳ chọn, nếu tách AI riêng bằng Python)
├── packages/
│   └── shared-types/      # Zod schema/DTO dùng chung FE-BE
├── docs/                    # thư mục này
├── docker-compose.yml
└── .github/workflows/
```
- Dùng **pnpm workspaces** hoặc **Turborepo** để quản lý monorepo nếu team quen; nếu không, dùng 2 repo riêng (`backend`, `frontend`) + repo `docs` liên kết — đơn giản hơn cho team lần đầu làm monorepo.
