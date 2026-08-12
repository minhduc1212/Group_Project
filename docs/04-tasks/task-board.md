# Task Board & Master Sprint Plan — 6 Thành Viên Chạy Song Song

> Xem bảng chia nhỏ micro-task chi tiết đến từng file & acceptance criteria ở **[TASKS.md](../TASKS.md)**.
> Board này theo dõi tiến độ tổng thể với **6 cột dọc theo 6 thành viên** (Tạ Quang Huy, Hà Đăng Huy, Phạm Đình Ánh Dương, Nguyễn Minh Đức, Nguyễn Tùng Dương, Đinh Tiến Luân).

## 1. Sprint 0 — Contract Session (ngày 1–2, bắt buộc cả 6 người)
Xem quy trình chi tiết ở [contract-first-workflow.md](../01-workflow/contract-first-workflow.md) và micro-tasks ở [TASKS.md](../TASKS.md) (TASK-001 đến TASK-008).
- [ ] TASK-001 `[BE-Core - Tạ Quang Huy]`: Chốt SQLAlchemy & Pydantic DB Schemas
- [ ] TASK-002 `[BE-Services - Phạm Đình Ánh Dương]`: FastAPI Controller Skeleton
- [ ] TASK-003 `[AI Lead - Nguyễn Tùng Dương & Tạ Quang Huy]`: LangGraph State & Fixture Data
- [ ] TASK-004 `[FE-Core - Hà Đăng Huy]`: MSW Mock Handlers Core APIs
- [ ] TASK-005 `[FE-Growth - Nguyễn Minh Đức]`: MSW Mock Handlers Streaming AI
- [ ] TASK-006 `[DevOps/Sec - Đinh Tiến Luân]`: Docker Compose & Environment
- [ ] TASK-007 `[DevOps/Sec - Đinh Tiến Luân]`: CI/CD GitHub Actions Pipeline
- [ ] TASK-008 `[DevOps/Sec - Đinh Tiến Luân]`: Pre-commit Hooks & Ruff setup

**Mốc ra khỏi Sprint 0**: contract đã push lên `main`, mọi người có thể code song song từ đây.

## 2. Sprint 1–4 — 6 Track Chạy Song Song

| Track / Thành viên | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
|---|---|---|---|---|
| **BE-Core & AI Tooling**<br>*(Tạ Quang Huy)* | DB Models & Alembic Migration (101) | Event/Plan CRUD + RolesGuard | Vote Engine + Plan Status (DRAFT→VOTING→CONFIRMED) | Realtime WS/SSE (402) + Token Logging (403) + Pytest coverage ≥ 70% |
| **BE-Platform & FE-Core**<br>*(Hà Đăng Huy)* | HTTPX Async + Redis Cache / Auth UI | Places API (Category Filter) + Weather/Currency / Event Dashboard + Mapbox | Manual Plan Builder + Vote UI | Component Testing + Polish Responsive UI |
| **BE-Services**<br>*(Phạm Đình Ánh Dương)* | Base Services (002) + Auth APIs (102–106) + Forgot/Reset Email (105) | Invitation APIs (203) | Email Notifications (SMTP) + PDF Export (WeasyPrint) | Admin APIs + Expense Splitting & Settlement (404, 405, 415) |
| **FE-Growth**<br>*(Nguyễn Minh Đức)* | Landing Page + i18n Setup (VI/EN) | UI AI Chat Mock + Category Cards | Checklist UI + PDF Download Preview | Streaming AI Chat UI + Shared Expenses + Admin UI |
| **AI Lead**<br>*(Nguyễn Tùng Dương)* | LangGraph Python Orchestrator + DeepSeek Wrapper | Location Agent + Research Agent + Note Agent | Plan Agent (DeepSeek-R1) + Cost + Conflict Resolver | Realtime Chat Agent (401) |
| **DevOps & Security**<br>*(Đinh Tiến Luân)* | FastAPI Security Middlewares + Ruff/CI | External API Security & Retry Review | Input Validation & Pydantic Output Defense Audit | Pentest OWASP Top 10 + Staging & Production Deploy |

> Chi tiết từng task (mã task `TASK-xxx`, file cần sửa, acceptance criteria), xem tại **[TASKS.md](../TASKS.md)**.

## 3. Bảng Theo Dõi Cá Nhân (6 Thành Viên)

| Thành viên | Phân công vai trò | Task file chi tiết | Micro-tasks | Trạng thái | Blocker |
|---|---|---|---|---|---|
| **Tạ Quang Huy** | Backend Dev A (Core Domain) & AI Integration | [person-1-backend-core.md](person-1-backend-core.md) | TASK-001, TASK-101, TASK-201..202, TASK-204, TASK-301..306, TASK-402..403 | 🟡-TO DO | — |
| **Hà Đăng Huy** | Backend Dev B (Platform) & Frontend Dev A (Core UI) | [person-2-backend-platform.md](person-2-backend-platform.md) / [person-4-frontend-core.md](person-4-frontend-core.md) | TASK-107..108, TASK-205..208, TASK-004, TASK-111..113, TASK-212..215, TASK-314..316 | 🔲 To Do | — |
| **Phạm Đình Ánh Dương** | Backend Dev C (Services & Settlement) | [person-2-backend-platform.md](person-2-backend-platform.md) | TASK-002, TASK-102..106, TASK-203, TASK-311..313, TASK-404..405, TASK-415 | 🔲 To Do | — |
| **Nguyễn Minh Đức** | Frontend Dev B (AI Experience & Growth UI) | [person-5-frontend-growth.md](person-5-frontend-growth.md) | TASK-005, TASK-009, TASK-010..011, TASK-114..115, TASK-317, TASK-406..410 | 🔲 To Do | — |
| **Nguyễn Tùng Dương** | AI Agent Lead (LangGraph Multi-Agent) | [person-3-ai-engineer.md](person-3-ai-engineer.md) | TASK-003, TASK-109..110, TASK-209..211, TASK-307..310, TASK-401 | 🔲 To Do | — |
| **Đinh Tiến Luân** | Cyber Security & DevOps Engineer | [person-6-security-devops.md](person-6-security-devops.md) | TASK-006..008, TASK-116..118, TASK-216, TASK-411..414 | 🔲 To Do | — |

Chú thích: 🔲 To Do · 🟡 In Progress · 🔵 In Review · ✅ Done · 🔴 Blocked
