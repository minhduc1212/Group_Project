# 🗺️ Hướng Dẫn Bắt Đầu & Lộ Trình Đọc Tài Liệu (guides.md)

Chào mừng bạn đến với dự án **Web Lên Kế Hoạch Nhóm Tích Hợp AI Multi-Agent**! 

Dự án có bộ tài liệu rất đầy đủ (hơn 30 file). Nếu bạn mới vào team hoặc lần đầu xem repo, **đừng đọc hết tất cả cùng lúc**. Hãy làm theo hướng dẫn dưới đây để biết chính xác cần đọc gì theo vai trò của mình.

---

## 🧭 1. Bạn Là Ai? Chọn Lộ Trình Đọc Docs (15 Phút)

### 🅰️ Giám Khảo / Mentor / Người Xem Dự Án (Reviewer & Evaluator)
> **Mục tiêu**: Hiểu nhanh dự án làm gì, độ phức tạp kỹ thuật ra sao, tính năng có gì hay.

1. Đọc **[README.md](README.md)** (2 phút) — Tổng quan mục lục và định hướng.
2. Đọc **[feature.md](feature.md)** (3 phút) — Xem danh sách 42 tính năng phân theo 7 nhóm.
3. Đọc **[explain.md](explain.md)** (5 phút) — Xem các luồng chạy thực tế (`TRAVEL`, `DINING`, `ENTERTAINMENT`...) và cách dùng DeepSeek API.
4. Đọc **[system-architecture.md](docs/03-architecture/system-architecture.md)** (3 phút) — Xem sơ đồ tổng thể Python FastAPI + React + Redis + Postgres + LangGraph.
5. Đọc **[TASKS.md](docs/TASKS.md)** (2 phút) — Xem bảng phân rã task chi tiết đến từng file.

---

### 🅱️ Backend Dev A — Core Domain (Auth, Event, Plan, Vote, Invitations)
> **Mục tiêu**: Nắm DB schema, API spec và các task core backend mình sở hữu.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Hiểu cơ chế code song song từ ngày 1 bằng API contract.
2. Đọc **[database-schema.md](docs/03-architecture/database-schema.md)** (5 phút) — Nắm kỹ các model SQLAlchemy: User, Event, Plan, PlanStop, PlanVote, Invitation.
3. Đọc **[api-design-guide.md](docs/02-standards/api-design-guide.md)** (3 phút) — Nắm các endpoint REST `/auth/*`, `/events/*`, `/invitations/*`, `/plans/*`, `/votes/*`.
4. Mở **[person-1-backend-core.md](docs/04-tasks/person-1-backend-core.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` mình phụ trách.

---

### 🅲️ Backend Dev B — Platform & Integration (Places API, Weather, Export, Admin)
> **Mục tiêu**: Nắm cách tích hợp Google Places, Redis cache, gửi mail, xuất PDF và Admin APIs.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Hiểu cách trả API spec để AI Engineer và FE dùng.
2. Đọc **[api-design-guide.md](docs/02-standards/api-design-guide.md)** (3 phút) — Xem endpoint `/places/*`, `/weather`, `/export/*`, `/admin/*`.
3. Đọc **[system-architecture.md](docs/03-architecture/system-architecture.md)** (3 phút) — Nắm cơ chế Redis Caching cho External APIs.
4. Mở **[person-2-backend-platform.md](docs/04-tasks/person-2-backend-platform.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` mình phụ trách.

---

### 🅳️ AI Engineer (LangGraph Multi-Agent System)
> **Mục tiêu**: Hiểu cấu trúc Agent graph, EventType routing, Pydantic state và DeepSeek models.

1. Đọc **[ai-agent-architecture.md](docs/03-architecture/ai-agent-architecture.md)** (7 phút) — Nắm mô hình Orchestrator-Worker, routing 6 EventType, LangGraph Python state.
2. Đọc **[explain.md](explain.md)** (5 phút) — Nắm sự phối hợp giữa `deepseek-chat` (V3) và `deepseek-reasoner` (R1).
3. Đọc **[database-schema.md](docs/03-architecture/database-schema.md)** (3 phút) — Nắm field `category` và `metadata` JSON của `PlanStop`.
4. Mở **[person-3-ai-engineer.md](docs/04-tasks/person-3-ai-engineer.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` mình phụ trách.

---

### 🅴️ Frontend Dev A — Core Flows UI (Auth, Event, Plan, Vote, Map)
> **Mục tiêu**: Nắm UI mockup, MSW mock setup, các màn hình Auth, Event, Plan Builder & Voting.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Hiểu cách dùng MSW mock API response để code UI ngay từ ngày 1.
2. Đọc **[api-design-guide.md](docs/02-standards/api-design-guide.md)** (3 phút) — Nắm shape dữ liệu trả về từ API.
3. Đọc **[coding-conventions.md](docs/02-standards/coding-conventions.md)** (3 phút) — Chuẩn React, TypeScript, TanStack Query, Tailwind.
4. Mở **[person-4-frontend-core.md](docs/04-tasks/person-4-frontend-core.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` mình phụ trách.

---

### 🅵️ Frontend Dev B — AI Experience & Growth (AI Chat UI, Landing, i18n, Admin UI)
> **Mục tiêu**: Nắm UI Chat AI streaming, Landing Page, đa ngôn ngữ, chia chi phí và Admin Dashboard UI.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Nắm cách mock streaming response cho AI Chat UI.
2. Đọc **[explain.md](explain.md)** (5 phút) — Nắm cách hiển thị các loại Card theo `StopCategory` (nhà hàng, chỗ chơi, tham quan...).
3. Mở **[person-5-frontend-growth.md](docs/04-tasks/person-5-frontend-growth.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` mình phụ trách.

---

### 🅶️ Cyber Security & DevOps
> **Mục tiêu**: Nắm hạ tầng Docker, CI/CD GitHub Actions, Pydantic Input/Output Validation & Security Middlewares.

1. Đọc **[security-guidelines.md](docs/05-security/security-guidelines.md)** (5 phút) — Checklist bảo mật OWASP, Pydantic sanitization, rate limit.
2. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (3 phút) — Quy trình review contract và dựng CI/CD từ Sprint 0.
3. Mở **[person-6-security-devops.md](docs/04-tasks/person-6-security-devops.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` mình phụ trách.

---

## 💻 2. Hướng Dẫn Chạy Môi Trường Dev Lần Đầu (5 Phút)

### Bước 1: Clone repo & chuẩn bị file môi trường
```bash
git clone <repo-url>
cd Group_Project
```

### Bước 2: Khởi động Backend (Python FastAPI)
```bash
cd backend
cp .env.example .env

# Khởi động PostgreSQL & Redis qua Docker
docker compose up -d

# Cài đặt dependency bằng Poetry (hoặc pip)
poetry install
poetry run alembic upgrade head

# Chạy server FastAPI dev (reload tự động)
poetry run uvicorn app.main:app --reload --port 8000
```
> Truy cập Swagger API Docs tại: `http://localhost:8000/docs`

### Bước 3: Khởi động Frontend (React + Vite)
```bash
cd ../frontend
npm install
npm run dev
```
> Truy cập Web UI tại: `http://localhost:5173`

---

## 🔄 3. Quy Trình Làm Việc & Bàn Giao Hàng Ngày (Cheatsheet)

```
1. Chọn Task      → Đọc docs/TASKS.md hoặc file task cá nhân (person-x-*.md)
2. Tạo Branch     → git checkout -b feature/TASK-102-mo-ta-ngan
3. Code & Test    → Code theo đúng Target Files & Acceptance Criteria. Run test passing.
4. Tick Done      → Đổi [ ] thành [x] trên file task cá nhân & docs/TASKS.md
5. Mở PR          → Push code, mở PR theo template, tag Reviewer / Buddy
6. Bàn giao       → Báo tin trên kênh #dev theo đúng quy trình bàn giao (cross-team-collaboration.md)
```

---

## 🗺️ 4. Bản Đồ Cây Tài Liệu (Sitemap Nhanh)

```
Group_Project/
├── README.md                          ← Điểm bắt đầu chính của Repository
├── guides.md                          ← BẠN ĐANG Ở ĐÂY (Hướng dẫn nhập môn & lộ trình đọc)
├── feature.md                         ← Danh sách 42 tính năng chuẩn hóa
├── explain.md                         ← Giải thích luồng vận hành chi tiết + DeepSeek API
├── CONTRIBUTING.md                    ← Quy định đóng góp code & tóm tắt bàn giao
├── .env.example                       ← Mẫu biến môi trường chuẩn
│
├── docs/
│   ├── TASKS.md                       ← 📌 BẢNG PHÂN RÃ MICRO-TASKS CHI TIẾT (TASK-001 -> TASK-414)
│   │
│   ├── 00-overview/                   ← Tổng quan dự án & nhân sự
│   │   ├── project-overview.md        ← Mục tiêu, scope MVP
│   │   ├── tech-stack.md              ← Công nghệ chi tiết (FastAPI, React, LangGraph)
│   │   └── team-roles.md              ← Phân vai trò 6 người & Ma trận RACI
│   │
│   ├── 01-workflow/                   ← Quy trình phối hợp team
│   │   ├── contract-first-workflow.md ← Quy trình làm song song từ ngày 1
│   │   ├── cross-team-collaboration.md← Thay đổi giữa chừng, giúp đỡ & BÀN GIAO CÔNG VIỆC
│   │   ├── git-workflow.md            ← Quy tắc branch, PR, merge
│   │   ├── branch-naming.md           ← Đặt tên branch
│   │   ├── commit-convention.md       ← Chuẩn commit message
│   │   └── code-review-checklist.md   ← Checklist review PR
│   │
│   ├── 02-standards/                  ← Tiêu chuẩn kỹ thuật
│   │   ├── coding-conventions.md      ← Python PEP8, FastAPI, Pydantic, React style
│   │   ├── naming-conventions.md      ← Quy tắc đặt tên biến/hàm/file
│   │   ├── api-design-guide.md        ← Chuẩn REST API endpoint & response format
│   │   ├── documentation-guide.md     ← Quy tắc viết tài liệu
│   │   └── testing-guide.md           ← Chuẩn viết Pytest & Vitest
│   │
│   ├── 03-architecture/               ← Kiến trúc kỹ thuật
│   │   ├── system-architecture.md     ← Sơ đồ tổng thể hệ thống
│   │   ├── database-schema.md         ← SQLAlchemy/Prisma DB Models & Indexes
│   │   └── ai-agent-architecture.md   ← LangGraph Python Multi-Agent Architecture
│   │
│   ├── 04-tasks/                      ← Task cá nhân theo 6 vai trò
│   │   ├── task-board.md              ← Bảng theo dõi tiến độ tổng 6 track
│   │   ├── person-1-backend-core.md   ← Backend Dev A (Auth, Event, Plan, Vote)
│   │   ├── person-2-backend-platform.md ← Backend Dev B (Places, Weather, Export, Admin)
│   │   ├── person-3-ai-engineer.md    ← AI Engineer (LangGraph Agents)
│   │   ├── person-4-frontend-core.md  ← Frontend Dev A (Core UI, Event/Plan)
│   │   ├── person-5-frontend-growth.md← Frontend Dev B (AI Chat UI, Landing, Admin UI)
│   │   └── person-6-security-devops.md← Cyber Security & DevOps
│   │
│   └── 05-security/                   ← Bảo mật
│       └── security-guidelines.md     ← Standard security checklist & Pydantic sanitization
```
