# Team & Roles — Mô hình Phân Công 6 Thành Viên Theo Vai Trò

## 1. Nguyên tắc phân công (chia theo Role & Nhân sự thực tế)
Dự án được phân chia theo **vai trò kỹ thuật (role)** với 6 thành viên phụ trách các mảng công việc chuyên biệt và kiêm nhiệm phù hợp:

- **Backend (3 người)**: Tạ Quang Huy, Hà Đăng Huy, Phạm Đình Ánh Dương
- **Frontend (2 người)**: Hà Đăng Huy, Nguyễn Minh Đức
- **Ai Agent (2 người)**: Nguyễn Tùng Dương, Tạ Quang Huy
- **DevOps & Security (1 người)**: Đinh Tiến Luân

Mỗi thành viên làm việc song song từ tuần 1 thông qua **hợp đồng giao diện (contract)** chốt trước — không phải chờ nhau theo trình tự. Xem cơ chế chi tiết ở [contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md).

## 2. 6 thành viên & phân công chi tiết

| # | Thành viên | Vai trò chính & kiêm nhiệm | Sở hữu mảng kỹ thuật | File task chi tiết |
|---|---|---|---|---|
| 1 | **Tạ Quang Huy** | **Backend Dev A (Core Domain)** & **AI Agent Integration** | N1 (Auth) + N2 (Event/Plan/Vote/Invitation) — Thiết kế Schema DB gốc + Bridge Tool Calling cho AI Agent | [person-1-backend-core.md](docs/04-tasks/person-1-backend-core.md) |
| 2 | **Hà Đăng Huy** | **Backend Dev B (Platform)** & **Frontend Dev A (Core UI)** | N3 (External API Google Places/Weather/Currency) + UI Auth, Event Dashboard, Plan Builder, Vote UI & Mapbox | [person-2-backend-platform.md](docs/04-tasks/person-2-backend-platform.md) / [person-4-frontend-core.md](docs/04-tasks/person-4-frontend-core.md) |
| 3 | **Phạm Đình Ánh Dương** | **Backend Dev C (Services & Realtime)** | N5 (Notification Email SMTP + PDF Export WeasyPrint) + Realtime WebSockets/SSE Server + N6 (Admin APIs) | [person-2-backend-platform.md](docs/04-tasks/person-2-backend-platform.md) |
| 4 | **Nguyễn Minh Đức** | **Frontend Dev B (AI Experience & Growth UI)** | UI Realtime Chat AI, Landing Page, i18n (VI/EN), Checklist UI, Shared Expenses Calculator, Admin Dashboard UI | [person-5-frontend-growth.md](docs/04-tasks/person-5-frontend-growth.md) |
| 5 | **Nguyễn Tùng Dương** | **AI Agent Lead (LangGraph & Multi-Agent)** | N4 (Toàn bộ Multi-Agent System: Orchestrator, Location, Research, Plan Agent DeepSeek-R1, Cost & Conflict Resolver) | [person-3-ai-engineer.md](docs/04-tasks/person-3-ai-engineer.md) |
| 6 | **Đinh Tiến Luân** | **DevOps & Cyber Security Engineer** | CI/CD GitHub Actions, Docker Compose, FastAPI Security Middlewares, Input Sanitization, Ruff/Black, Pentest OWASP Top 10 | [person-6-security-devops.md](docs/04-tasks/person-6-security-devops.md) |

## 3. Vì sao chia thế này chạy song song được?
| Vấn đề khi chia theo Nhóm cũ | Cách giải quyết khi chia theo Người |
|---|---|
| AI Agent (N4) phải chờ Backend (N2) xong schema | Tuần 1 cả team chốt chung **1 buổi contract session**: schema SQLAlchemy + OpenAPI spec. AI Agent (Nguyễn Tùng Dương & Tạ Quang Huy) code thẳng lên **mock server / fixtures** dựng từ contract đó |
| Frontend chờ Backend xong API mới code UI | Frontend (Hà Đăng Huy & Nguyễn Minh Đức) dùng **MSW (Mock Service Worker)** mock response theo đúng OpenAPI contract, code UI song song |
| Security chỉ "review sau cùng" | Security & DevOps (Đinh Tiến Luân) dựng CI/CD, Docker, viết rule lint bảo mật, threat-model hệ AI Agent chạy song song từ Sprint 0 |
| Phụ thuộc tiến độ giữa các mảng | Mỗi người có **backlog riêng rõ ràng**, không bị nghẽn hay gián đoạn công việc |

## 4. Ma trận phối hợp (RACI) — Theo thành viên thực tế

R = Responsible (Người thực hiện) · A = Accountable (Người chịu trách nhiệm) · C = Consulted (Người tham vấn) · I = Informed (Người nhận thông tin)

| Đầu việc | Tạ Quang Huy (BE Core/AI) | Hà Đăng Huy (BE Plat/FE Core) | Phạm Đình Ánh Dương (BE Serv) | Nguyễn Minh Đức (FE Growth) | Nguyễn Tùng Dương (AI Lead) | Đinh Tiến Luân (DevOps/Sec) |
|---|---|---|---|---|---|---|
| Contract API + DB Schema (Sprint 0) | **R/A** | C | C | C | C | C |
| Auth (login/OAuth/JWT) | **R/A** | **R** (UI) | I | I | I | **R** (review sec) |
| Event/Plan/Vote CRUD API | **R/A** | **R** (UI) | C | I | C (schema) | C |
| External API (Places/Weather) + Cache | I | **R/A** | C | I | C (dùng data) | I |
| Realtime SSE/WS, Email & PDF Export | I | I | **R/A** | C (UI Download) | C | C |
| AI Multi-Agent Architecture & Graphs | C (tools) | I | I | I | **R/A** | **R** (sec review) |
| AI Tool Calling & Data Bridge | **R/A** | C | I | I | C | I |
| UI Core Flows (Event/Plan/Vote/Map) | C | **R/A** | I | C | I | I |
| UI AI Chat / Landing / Expenses / Admin | I | C | C | **R/A** | C | I |
| CI/CD, Docker, Pentest & Security | I | I | I | I | I | **R/A** |

## 5. Đồng bộ giữa 6 thành viên
| Việc | Tần suất |
|---|---|
| Contract sync (đổi API/schema) | Bất cứ khi nào đổi — báo ngay kênh `#contract-changes`, không chờ họp |
| Daily update async | Mỗi ngày, 3 dòng: hôm qua/hôm nay/blocker |
| Weekly demo + đồng bộ contract | 1 buổi/tuần — mỗi người demo phần mình, đối chiếu contract |
| Integration day | Cuối mỗi sprint — nối Frontend thật với Backend thật (thay mock), AI Agent nối với DB thật |
