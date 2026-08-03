# Task Board & Master Sprint Plan — 6 Track Run Parallel

> Xem bảng chia nhỏ micro-task chi tiết đến từng file & acceptance criteria ở **[TASKS.md](../TASKS.md)**.
> Board này theo dõi tiến độ tổng thể với **6 cột dọc theo người** (BE-A, BE-B, AI, FE-A, FE-B, Security/DevOps).

## 1. Sprint 0 — Contract Session (ngày 1–2, bắt buộc cả 6 người)
Xem quy trình chi tiết ở [contract-first-workflow.md](../01-workflow/contract-first-workflow.md) và micro-tasks ở [TASKS.md](../TASKS.md) (TASK-001 đến TASK-008).
- [ ] TASK-001 `[BE-A]`: Chốt SQLAlchemy & Pydantic DB Schemas
- [ ] TASK-002 `[BE-A]`: FastAPI Controller Skeleton
- [ ] TASK-003 `[AI]`: LangGraph State & Fixture Data
- [ ] TASK-004 `[FE-A]`: MSW Mock Handlers Core APIs
- [ ] TASK-005 `[FE-B]`: MSW Mock Handlers Streaming AI
- [ ] TASK-006 `[SEC/DEVOPS]`: Docker Compose & Environment
- [ ] TASK-007 `[SEC/DEVOPS]`: CI/CD GitHub Actions Pipeline
- [ ] TASK-008 `[SEC/DEVOPS]`: Pre-commit Hooks & Ruff setup

**Mốc ra khỏi Sprint 0**: contract đã push lên `main`, mọi người có thể code song song từ đây.

## 2. Sprint 1–4 — 6 Track Chạy Song Song

| Track | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
|---|---|---|---|---|
| **BE-A (Core)** | Auth API (OAuth2, JWT, Pydantic) | Event/Plan/Invitation CRUD + RolesGuard | Vote Engine + Plan Status (DRAFT→VOTING→CONFIRMED) | Hardening + Pytest coverage ≥ 70% |
| **BE-B (Platform)** | HTTPX Async + Redis Cache | Places API (Category Filter) + Weather/Currency | Email Notifications (SMTP) + PDF Export (WeasyPrint) | Admin Dashboard APIs + Token usage |
| **AI Engineer** | LangGraph Python Orchestrator + DeepSeek Wrapper | Location Agent + Research Agent + Note Agent | Plan Agent (DeepSeek-R1) + Cost + Conflict Resolver | Realtime Chat Agent + SSE/WebSocket Streaming |
| **FE-A (Core)** | Auth UI (Login, Register, Profile, MSW) | Event Dashboard + EventType Selector + Mapbox | Manual Plan Builder + Vote & Confirmation UI | Component Testing + Polish Responsive UI |
| **FE-B (Growth)** | Landing Page + i18n Setup (VI/EN) | UI AI Chat Mock + Category Cards | Checklist UI + PDF Download Preview | Streaming AI Chat UI + Shared Expenses + Admin UI |
| **Security/DevOps** | FastAPI Security Middlewares + Ruff/CI | External API Security & Retry Review | Input Validation & Pydantic Output Defense Audit | Pentest OWASP Top 10 + Staging & Production Deploy |

> Chi tiết từng task (mã task `TASK-xxx`, file cần sửa, acceptance criteria), xem tại **[TASKS.md](../TASKS.md)**.

## 3. Bảng Theo Dõi Cá Nhân

| Người | Task file chi tiết | Micro-tasks | Trạng thái | Blocker |
|---|---|---|---|---|
| Backend Dev A | [person-1-backend-core.md](person-1-backend-core.md) | TASK-001, TASK-101..106, TASK-201..204, TASK-301..306, TASK-404 | 🔲 To Do | — |
| Backend Dev B | [person-2-backend-platform.md](person-2-backend-platform.md) | TASK-107..108, TASK-205..208, TASK-311..313, TASK-405 | 🔲 To Do | — |
| AI Engineer | [person-3-ai-engineer.md](person-3-ai-engineer.md) | TASK-003, TASK-109..110, TASK-209..211, TASK-307..310, TASK-401..403 | 🔲 To Do | — |
| Frontend Dev A | [person-4-frontend-core.md](person-4-frontend-core.md) | TASK-004, TASK-111..113, TASK-212..215, TASK-314..317 | 🔲 To Do | — |
| Frontend Dev B | [person-5-frontend-growth.md](person-5-frontend-growth.md) | TASK-005, TASK-114..115, TASK-406..410 | 🔲 To Do | — |
| Security/DevOps | [person-6-security-devops.md](person-6-security-devops.md) | TASK-006..008, TASK-116..117, TASK-411..414 | 🔲 To Do | — |

Chú thích: 🔲 To Do · 🟡 In Progress · 🔵 In Review · ✅ Done · 🔴 Blocked
