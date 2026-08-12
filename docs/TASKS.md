# 📌 Master Detailed Task Breakdown (TASKS.md)
## Dự án: Web Lên Kế Hoạch Nhóm Tích Hợp AI Multi-Agent
**Tech Stack**: Python 3.11+ FastAPI (Backend) · LangGraph Python (AI Multi-Agent) · React 18 + Vite + TS (Frontend) · PostgreSQL + Redis · DeepSeek API (V3 & R1)

---

## 📊 Quick Status Overview

| Sprint | Focus | Total Micro-Tasks | Status |
|---|---|---|---|
| **Sprint 0** | Contract Session, DB Models, OpenAPI Spec, UI/UX Design, Docker & CI/CD | 11 Tasks | 🔲 To Do |
| **Sprint 1** | Auth Module, Base External APIs, Orchestrator Skeleton, Core UI Foundations, Vercel Deploy | 18 Tasks | 🔲 To Do |
| **Sprint 2** | Event/Plan/Invitation CRUD, Places/Weather API, Location & Research Agents, UI Event/Plan, Render Deploy | 16 Tasks | 🔲 To Do |
| **Sprint 3** | Vote Engine, Manual Plan Flow, Plan/Cost/Conflict Agents, Export PDF & Notifications | 17 Tasks | 🔲 To Do |
| **Sprint 4** | Streaming AI Chat UI, Shared Expenses, Admin Dashboard, Security Pentest & Hardening | 15 Tasks | 🔲 To Do |
| **Tổng cộng** | 5 Sprint | **77 Tasks** | |

---

## 👥 Team & Task Mapping Legend

| Tag Code | Domain / Vai trò | Thành viên phụ trách | File task chi tiết |
|---|---|---|---|
| `[BE-A]` / `[BE-Core]` | Backend Core Domain & DB Schema | **Tạ Quang Huy** | [person-1-backend-core.md](04-tasks/person-1-backend-core.md) |
| `[BE-B]` / `[BE-Platform]` | External APIs (Places/Weather) & Redis Cache | **Hà Đăng Huy** | [person-2-backend-platform.md](04-tasks/person-2-backend-platform.md) |
| `[BE-Services]` | Auth, Email, PDF Export, Invitations, Expense & Settlement, Admin | **Phạm Đình Ánh Dương** | [person-2-backend-platform.md](04-tasks/person-2-backend-platform.md) |
| `[FE-A]` / `[FE-Core]` | Frontend Core Flows UI (Auth, Event, Plan, Map) | **Hà Đăng Huy** | [person-4-frontend-core.md](04-tasks/person-4-frontend-core.md) |
| `[FE-B]` / `[FE-Growth]` | Frontend AI Chat UI, Shared Expenses & Admin | **Nguyễn Minh Đức** | [person-5-frontend-growth.md](04-tasks/person-5-frontend-growth.md) |
| `[AI]` | AI Multi-Agent Architecture & Integration | **Nguyễn Tùng Dương** (Lead) & **Tạ Quang Huy** (Tooling) | [person-3-ai-engineer.md](04-tasks/person-3-ai-engineer.md) |
| `[SEC/DEVOPS]` | Cyber Security & DevOps (CI/CD, Docker, Pentest) | **Đinh Tiến Luân** | [person-6-security-devops.md](04-tasks/person-6-security-devops.md) |

---

## 🛠️ Sprint 0 — Contract Session & Infrastructure Setup

### 0.1 Architecture & Contract Definition
- [ ] **TASK-001** `[BE-A]` **Design SQLAlchemy & Pydantic Schemas**
  - **Feature**: N/A (Sprint 0 Contract)
  - **Target Files**: `backend/app/models/` (`user.py`, `event.py`, `plan.py`, `vote.py`, `invitation.py`, `log.py`, **`expense.py`, `settlement.py`**), `backend/app/schemas/`
  - **Acceptance Criteria**: Full support for `EventType`, `StopCategory`, `metadata` JSON, `Invitation`, `PlanStatus`. Đủ 3 bảng tài chính trong [database-schema.md](03-architecture/database-schema.md): `expenses`, `expense_splits`, `settlements` (thu quỹ = `Expense.type=ADVANCE`, số dư member tính bằng SQL GROUP BY — không cần bảng MemberBalance) + `total_budget` trên Plan / `estimated_cost` trên PlanStop. Migration passes clean via Alembic.
- [ ] **TASK-002** `[BE-Services]` **FastAPI APIRouter Skeleton**
  - **Feature**: N/A (Contract)
  - **Target Files**: `backend/app/api/v1/` (`auth.py`, `events.py`, `plans.py`, `votes.py`, `invitations.py`, `places.py`, `ai.py`)
  - **Acceptance Criteria**: Routes return `501 Not Implemented` with matching Pydantic response models. Swagger accessible at `http://localhost:8000/docs`.
- [ ] **TASK-003** `[AI]` **LangGraph State & Fixture Fixtures Definition**
  - **Feature**: #23
  - **Target Files**: `backend/app/ai_agents/state.py`, `backend/app/ai_agents/fixtures/` (`mock_places.json`, `mock_plans.json`)
  - **Acceptance Criteria**: Define Pydantic `AgentState`. Mock fixtures validate cleanly against DB schemas.
- [ ] **TASK-004** `[FE-A]` **MSW Mock Handlers Setup for Core APIs**
  - **Feature**: N/A
  - **Target Files**: `frontend/src/mocks/handlers/` (`auth.ts`, `events.ts`, `plans.ts`)
  - **Acceptance Criteria**: MSW intercepts `/api/v1/auth/*` and `/api/v1/events/*`, returning mock JSON adhering to OpenAPI contract.
- [ ] **TASK-005** `[FE-B]` **MSW Streaming Mock Setup for AI Chat**
  - **Feature**: #31, #32
  - **Target Files**: `frontend/src/mocks/handlers/ai.ts`
  - **Acceptance Criteria**: Simulates SSE / WebSocket chunked responses for chat UI testing without calling real backend.
- [ ] **TASK-006** `[SEC/DEVOPS]` **Docker Compose & Environment Setup**
  - **Feature**: N/A
  - **Target Files**: `docker-compose.yml`, `backend/Dockerfile`, `.env.example`
  - **Acceptance Criteria**: `docker compose up -d` starts PostgreSQL 15, Redis 7, FastAPI server without errors.

### 0.2 CI/CD & Code Quality Rules
- [ ] **TASK-007** `[SEC/DEVOPS]` **GitHub Actions Pipeline Setup**
  - **Feature**: N/A
  - **Target Files**: `.github/workflows/ci.yml`
  - **Acceptance Criteria**: Automated runs on PR: `ruff check backend`, `mypy backend`, `pytest backend`, `pnpm run lint frontend`, `pnpm run build frontend`.
- [ ] **TASK-008** `[SEC/DEVOPS]` **Pre-commit Hooks & Linter Setup**
  - **Feature**: N/A
  - **Target Files**: `.pre-commit-config.yaml`, `backend/pyproject.toml`
  - **Acceptance Criteria**: Blocks local git commit if Ruff linting fails or Black formatting drifts.

### 0.3 UI/UX Design (Sprint 0 — làm trước khi bắt đầu code giao diện)
> Làm song song với Contract Session. Kết quả là **nguồn chân lý thiết kế** cho FE Dev A & B xuyên suốt các Sprint sau. Tài liệu thiết kế lưu tại `docs/06-design/`.
- [ ] **TASK-009** `[FE-B]` **Design Tokens & Design System Spec**
  - **Feature**: #42
  - **Target Files**: `docs/06-design/design-tokens.md`, `frontend/src/styles/theme.ts`, `frontend/tailwind.config.js`
  - **Acceptance Criteria**: Chốt palette (light/dark), typography scale, spacing, radius, shadow; mapping sang shadcn/Tailwind theme config; được dùng làm nguồn duy nhất cho mọi màn hình (feed vào TASK-111).
- [ ] **TASK-010** `[FE-B]` **User Flows & Page Wireframes**
  - **Feature**: #1 → #42
  - **Target Files**: `docs/06-design/user-flows.md`, `docs/06-design/wireframes/` (Mermaid/ASCII hoặc Figma)
  - **Acceptance Criteria**: Flowchart các luồng chính: register/login → tạo event → mời member → tạo/vote plan → confirm → chia chi phí; wireframe từng page chốt layout + component + empty/loading/error state.
- [ ] **TASK-011** `[FE-B]` **Hi-fi Mockups, Component Library & Accessibility**
  - **Feature**: #42
  - **Target Files**: `docs/06-design/mockups.md` (link Figma), `frontend/src/components/ui/` (variants)
  - **Acceptance Criteria**: Hi-fi mockups cho 6 EventType + AI chat streaming + expense/settlement; component variants (Button/Input/Card/Dialog/Toast) theo design tokens; responsive breakpoints (mobile/tablet/desktop) + contrast WCAG AA.

---

## 🔐 Sprint 1 — Auth & Core Infrastructure

### 1.1 Auth & User Management (Backend Core & Services)
- [ ] **TASK-101** `[BE-A]` **Database Models & Alembic Initial Migration**
  - **Feature**: #2, #4
  - **Target Files**: `backend/app/models/user.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: User table created with `id`, `email`, `password_hash`, `full_name`, `avatar_url`, `provider`.
- [ ] **TASK-102** `[BE-Services]` **User Registration & Password Hashing**
  - **Feature**: #2
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/services/auth_service.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/register` validates Pydantic schema, hashes password using `passlib[bcrypt]`, returns user JWT tokens.
- [ ] **TASK-103** `[BE-Services]` **OAuth2 Integration (Google & Facebook)**
  - **Feature**: #1
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/core/oauth.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/login/google` exchanges auth code for token, creates or logs in user, returns JWT access/refresh token.
- [ ] **TASK-104** `[BE-Services]` **JWT Access & Refresh Token Rotation**
  - **Feature**: #5
  - **Target Files**: `backend/app/core/security.py`, `backend/app/api/v1/auth.py`
  - **Acceptance Criteria**: Access token expires in 15 mins. `POST /api/v1/auth/refresh-token` validates refresh token in httpOnly cookie and issues new pair.
- [ ] **TASK-105** `[BE-Services]` **Forgot & Reset Password Flow**
  - **Feature**: #3
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/services/email_service.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/forgot-password` generates single-use 15-min token and sends email via SMTP.
- [ ] **TASK-106** `[BE-Services]` **User Profile API (GET & PATCH)**
  - **Feature**: #4
  - **Target Files**: `backend/app/api/v1/users.py`, `backend/app/services/user_service.py`
  - **Acceptance Criteria**: `GET /api/v1/users/me` returns current user profile; `PATCH /api/v1/users/me` updates `full_name`, `avatar_url`.

### 1.2 Platform & External Integration Baseline
- [ ] **TASK-107** `[BE-B]` **HTTPX Async Client & Redis Caching Service**
  - **Feature**: #22
  - **Target Files**: `backend/app/core/redis.py`, `backend/app/services/cache_service.py`
  - **Acceptance Criteria**: Generic cache decorator `cache_response(ttl=3600)` stores and retrieves JSON responses from Redis.
- [ ] **TASK-108** `[BE-B]` **Google Places API Base Service**
  - **Feature**: #17
  - **Target Files**: `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `PlacesService.search_places()` queries Google Places API using `httpx.AsyncClient` and caches in Redis.

### 1.3 AI Multi-Agent Orchestrator Baseline
- [ ] **TASK-109** `[AI]` **LangGraph Orchestrator Skeleton**
  - **Feature**: #23
  - **Target Files**: `backend/app/ai_agents/orchestrator.py`
  - **Acceptance Criteria**: Graph builds state, routes intent to dummy sub-agents based on `EventType`, respects `recursion_limit=15`.
- [ ] **TASK-110** `[AI]` **DeepSeek API Provider Wrapper**
  - **Feature**: #23, #31
  - **Target Files**: `backend/app/ai_agents/llm_provider.py`
  - **Acceptance Criteria**: Wraps `deepseek-chat` and `deepseek-reasoner` with retry logic, rate limiting, and token logging.

### 1.4 Frontend Core Foundations & Auth UI
- [ ] **TASK-111** `[FE-A]` **Project Skeleton & Design System (Tailwind + shadcn)**
  - **Feature**: #42
  - **Target Files**: `frontend/src/`, `frontend/tailwind.config.js`
  - **Acceptance Criteria**: Vite app builds cleanly with Tailwind CSS, shadcn components (Button, Input, Card, Dialog), responsive design.
- [ ] **TASK-112** `[FE-A]` **Login & Register UI Screens**
  - **Feature**: #1, #2
  - **Target Files**: `frontend/src/features/auth/pages/LoginPage.tsx`, `RegisterPage.tsx`
  - **Acceptance Criteria**: Form validation with React Hook Form + Zod, Google/Facebook login buttons, submit calls Auth API / MSW.
- [ ] **TASK-113** `[FE-A]` **Forgot Password & Profile Management UI**
  - **Feature**: #3, #4
  - **Target Files**: `frontend/src/features/auth/pages/ForgotPasswordPage.tsx`, `ProfilePage.tsx`
  - **Acceptance Criteria**: Profile page allows avatar upload and name edit, updates Zustand auth store.
- [ ] **TASK-114** `[FE-B]` **Landing Page & Hero Section**
  - **Feature**: #39
  - **Target Files**: `frontend/src/features/landing/pages/LandingPage.tsx`
  - **Acceptance Criteria**: Showcases 6 event types (Travel, Dining, Hangout, Entertainment, Sightseeing, Custom) with CTA buttons.
- [ ] **TASK-115** `[FE-B]` **i18n Setup (react-i18next)**
  - **Feature**: #40
  - **Target Files**: `frontend/src/i18n/`, `frontend/src/locales/` (`vi.json`, `en.json`)
  - **Acceptance Criteria**: Header language toggle switches entire UI seamlessly between Vietnamese and English.

### 1.5 Security & Middleware Setup
- [ ] **TASK-116** `[SEC/DEVOPS]` **FastAPI Security Middlewares**
  - **Feature**: Security Baseline
  - **Target Files**: `backend/app/main.py`
  - **Acceptance Criteria**: Configures `CORSMiddleware` (restricted origins), `TrustedHostMiddleware`, security headers via middleware.
- [ ] **TASK-117** `[SEC/DEVOPS]` **Auth Module Security Review**
  - **Feature**: Security
  - **Target Files**: `backend/app/api/v1/auth.py`
  - **Acceptance Criteria**: Sign-off on bcrypt cost factor ≥ 10, JWT secret length ≥ 32 chars, httpOnly cookie settings, rate limit configuration.

### 1.6 Frontend Deployment — Vercel (CI/CD)
> Tương ứng feature "Hosting Frontend | **Vercel**" trong [tech-stack.md](../00-overview/tech-stack.md). Chi tiết cấu hình xem [deployment-guide.md](../03-architecture/deployment-guide.md). **Frontend deploy từ Sprint 1** vì TASK-113 đã có UI base — không chờ đến cuối dự án.
- [ ] **TASK-118** `[SEC/DEVOPS]` **Vercel Deploy Pipeline (Preview + Production)**
  - **Feature**: N/A (Deployment)
  - **Target Files**: `vercel.json`, `.github/workflows/cd-frontend.yml`, `docs/03-architecture/deployment-guide.md`
  - **Acceptance Criteria**: Mỗi PR tạo **Preview URL** riêng; merge vào `main` tự động deploy **Production**. Cấu hình biến môi trường theo env: `VITE_API_BASE_URL` (Preview → staging, Production → Render domain), `VITE_USE_MOCK=false`, `VITE_MAPBOX_ACCESS_TOKEN`. Smoke test URL live sau deploy (build pass + trang tải được + không lỗi runtime).
  - **Definition of Done**: `vercel.json` chốt build command + output dir + headers; CD workflow chạy `pnpm build` + upload build; link project trên Vercel team.

---

## 📅 Sprint 2 — Event, Plan & External Integrations

### 2.1 Event & Invitation Management (Backend Core & Services)
- [ ] **TASK-201** `[BE-A]` **Event Database Models & Alembic Migration**
  - **Feature**: #6
  - **Target Files**: `backend/app/models/event.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: Tables `events` and `event_members` created with `EventType` enum (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM) and `EventRole` enum (OWNER, MEMBER, VIEWER).
- [ ] **TASK-202** `[BE-A]` **Event CRUD APIs**
  - **Feature**: #6, #9
  - **Target Files**: `backend/app/api/v1/events.py`, `backend/app/services/event_service.py`
  - **Acceptance Criteria**: `POST /events` creates event and assigns creator as `OWNER`. `GET /events` lists user events. `PATCH /events/{id}` updates event info.
- [ ] **TASK-203** `[BE-Services]` **Invitation Database Model & APIs**
  - **Feature**: #7
  - **Target Files**: `backend/app/models/invitation.py`, `backend/app/api/v1/invitations.py`
  - **Acceptance Criteria**: `POST /events/{id}/invitations` generates invitation link / email. `PATCH /invitations/{id}` allows user to ACCEPT or DECLINE. Joining adds entry to `event_members`.
- [ ] **TASK-204** `[BE-A]` **RolesGuard Dependency (Owner / Member / Viewer)**
  - **Feature**: #8
  - **Target Files**: `backend/app/api/v1/dependencies.py`
  - **Acceptance Criteria**: Reusable FastAPI dependency `require_role(min_role)` raises `403 Forbidden` if user lacks permissions.

### 2.2 External Integrations & Caching (Backend Platform)
- [ ] **TASK-205** `[BE-B]` **Google Places Search with Category Filter**
  - **Feature**: #17
  - **Target Files**: `backend/app/api/v1/places.py`, `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `GET /api/v1/places/search?category=RESTAURANT|CAFE|ENTERTAINMENT|ATTRACTION` filters Google Places API response and attaches category metadata.
- [ ] **TASK-206** `[BE-B]` **Hotel Data Comparison Service**
  - **Feature**: #18
  - **Target Files**: `backend/app/api/v1/places.py`, `backend/app/services/hotel_service.py`
  - **Acceptance Criteria**: `GET /api/v1/hotels/compare?ids=...` compares price, rating, amenities of hotels side-by-side.
- [ ] **TASK-207** `[BE-B]` **OpenWeatherMap Integration Service**
  - **Feature**: #20
  - **Target Files**: `backend/app/api/v1/utils.py`, `backend/app/services/weather_service.py`
  - **Acceptance Criteria**: `GET /api/v1/weather?lat=&lng=` returns forecast, temperature, weather conditions. Cached for 3 hours.
- [ ] **TASK-208** `[BE-B]` **Currency Converter API**
  - **Feature**: #21
  - **Target Files**: `backend/app/api/v1/utils.py`, `backend/app/services/currency_service.py`
  - **Acceptance Criteria**: `GET /api/v1/exchange-rate?from=USD&to=VND` fetches live exchange rates with 12h Redis cache.

### 2.3 AI Location, Research & Note Agents
- [ ] **TASK-209** `[AI]` **Location Agent Implementation**
  - **Feature**: #24
  - **Target Files**: `backend/app/ai_agents/agents/location_agent.py`
  - **Acceptance Criteria**: Receives category filter and preferences, queries `PlacesService`, returns top 5 structured place suggestions.
- [ ] **TASK-210** `[AI]` **Research Agent Implementation**
  - **Feature**: #25
  - **Target Files**: `backend/app/ai_agents/agents/research_agent.py`
  - **Acceptance Criteria**: Fetches place reviews, generates menu suggestions for DINING, activity ticket prices for ENTERTAINMENT, opening hours for SIGHTSEEING.
- [ ] **TASK-211** `[AI]` **Note Agent Implementation**
  - **Feature**: #28
  - **Target Files**: `backend/app/ai_agents/agents/note_agent.py`
  - **Acceptance Criteria**: Combines weather forecast with destination type to generate smart travel/hangout tips.

### 2.4 Event & Plan UI Screens (Frontend Core)
- [ ] **TASK-212** `[FE-A]` **Event Creation Dialog & EventType Selector**
  - **Feature**: #6
  - **Target Files**: `frontend/src/features/event/components/CreateEventModal.tsx`
  - **Acceptance Criteria**: Form allows selecting `EventType` (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM), dates, location.
- [ ] **TASK-213** `[FE-A]` **Event List & Event Detail Dashboard UI**
  - **Feature**: #9
  - **Target Files**: `frontend/src/features/event/pages/EventListPage.tsx`, `EventDetailPage.tsx`
  - **Acceptance Criteria**: Displays event cards, status badges, member list, navigation tabs (Plans, Members, Chat, Settings).
- [ ] **TASK-214** `[FE-A]` **Member Invitation Modal & Pending List UI**
  - **Feature**: #7
  - **Target Files**: `frontend/src/features/event/components/InviteMemberModal.tsx`
  - **Acceptance Criteria**: Allows sending email/link invites, displays pending invitations list with status (Pending/Accepted/Declined).
- [ ] **TASK-215** `[FE-A]` **Interactive Map Component (Mapbox Integration)**
  - **Feature**: #19
  - **Target Files**: `frontend/src/components/map/MapView.tsx`
  - **Acceptance Criteria**: Renders markers for plan stops, centers camera dynamically, shows popup details on marker click.

### 2.5 Backend Deployment — Render (CI/CD)
> Tương ứng feature "Hosting Backend | **Render / Railway / VPS**" trong [tech-stack.md](../00-overview/tech-stack.md). Chi tiết cấu hình xem [deployment-guide.md](../03-architecture/deployment-guide.md). **Backend deploy từ Sprint 2** — sau khi có Event/Plan CRUD thật, để Integration Day cuối Sprint 2 Frontend bỏ mock trỏ API thật.
- [ ] **TASK-216** `[SEC/DEVOPS]` **Render Deploy Pipeline (FastAPI + Postgres + Redis)**
  - **Feature**: N/A (Deployment)
  - **Target Files**: `render.yaml`, `backend/Dockerfile.prod`, `.github/workflows/cd-backend.yml`, `docs/03-architecture/deployment-guide.md`
  - **Acceptance Criteria**: Render Blueprint (`render.yaml`) khởi tạo FastAPI web service + PostgreSQL 15 + Redis 7. Deploy tự động khi merge vào `main`. Chạy `alembic upgrade head` trong quá trình deploy. `/health` trả green. Secrets (JWT, DB URL, AI keys, email) cấu hình qua Render env, **không** hardcode/.env commit.
  - **Definition of Done**: `Dockerfile.prod` dùng non-root user + multi-stage; CD workflow build image + push; smoke test curl `/health` sau deploy.

---

## 🗳️ Sprint 3 — Voting System, Plan Generation & Exports

### 3.1 Plan & Vote Engine (Backend Core)
- [ ] **TASK-301** `[BE-A]` **Plan & PlanStop Models with Category Metadata**
  - **Feature**: #10, #11, #12
  - **Target Files**: `backend/app/models/plan.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: Tables `plans`, `plan_stops`, `plan_votes` created with `created_by_id`, `is_ai_generated`, `PlanStatus` enum (DRAFT, VOTING, CONFIRMED, ARCHIVED), `StopCategory` enum, `metadata` JSON.
- [ ] **TASK-302** `[BE-A]` **Manual Plan Creation API**
  - **Feature**: #11
  - **Target Files**: `backend/app/api/v1/plans.py`, `backend/app/services/plan_service.py`
  - **Acceptance Criteria**: `POST /events/{id}/plans` with `is_ai_generated=False` creates manual plan with initial status `DRAFT`.
- [ ] **TASK-303** `[BE-A]` **Plan Stop Management API (Reorder / Add / Delete / Edit)**
  - **Feature**: #12
  - **Target Files**: `backend/app/api/v1/plans.py`
  - **Acceptance Criteria**: `PATCH /events/{id}/plans/{planId}/stops` supports reordering stop sequence, updating notes, cost, and JSON metadata.
- [ ] **TASK-304** `[BE-A]` **Plan Vote API & Tallying Logic**
  - **Feature**: #13
  - **Target Files**: `backend/app/api/v1/votes.py`, `backend/app/services/vote_service.py`
  - **Acceptance Criteria**: `POST /events/{id}/plans/{planId}/votes` allows voting UP, DOWN, NEUTRAL with optional comment. Enforces unique constraint per `(plan_id, user_id)`.
- [ ] **TASK-305** `[BE-A]` **Plan Status Transition API (DRAFT → VOTING → CONFIRMED)**
  - **Feature**: #14
  - **Target Files**: `backend/app/api/v1/plans.py`
  - **Acceptance Criteria**: Creator can set `VOTING`. Only `OWNER` can confirm plan (`CONFIRMED`). Updates plan status and locks confirmed version.
- [ ] **TASK-306** `[BE-A]` **Saved Places API**
  - **Feature**: #15
  - **Target Files**: `backend/app/api/v1/saved_places.py`
  - **Acceptance Criteria**: `POST /saved-places` saves favorite restaurant, place, or venue to user's saved list.

### 3.2 AI Planning, Costing & Conflict Resolution Agents
- [ ] **TASK-307** `[AI]` **Plan Agent Implementation (DeepSeek-R1)**
  - **Feature**: #26
  - **Target Files**: `backend/app/ai_agents/agents/plan_agent.py`
  - **Acceptance Criteria**: Uses `deepseek-reasoner` to build optimal stop sequence, time allocation, and daily budget based on event type.
- [ ] **TASK-308** `[AI]` **Cost Agent Implementation**
  - **Feature**: #29
  - **Target Files**: `backend/app/ai_agents/agents/cost_agent.py`
  - **Acceptance Criteria**: Calculates total budget, per-person split, and per-item breakdown.
- [ ] **TASK-309** `[AI]` **Conflict Resolver Agent Implementation (DeepSeek-R1)**
  - **Feature**: #30
  - **Target Files**: `backend/app/ai_agents/agents/conflict_agent.py`
  - **Acceptance Criteria**: Analyzes vote comments and negative votes, generates a compromised draft plan resolving objections.
- [ ] **TASK-310** `[AI]` **Booking Agent Implementation**
  - **Feature**: #27
  - **Target Files**: `backend/app/ai_agents/agents/booking_agent.py`
  - **Acceptance Criteria**: Returns direct booking URLs for hotels (Booking.com / Agoda), restaurant reservations, or activity tickets without performing payment.

### 3.3 Notifications & Export (Backend Services)
- [ ] **TASK-311** `[BE-Services]` **Email Notification Service (SMTP)**
  - **Feature**: #33
  - **Target Files**: `backend/app/services/notification_service.py`
  - **Acceptance Criteria**: Sends email notifications when invited to event, when plan vote opens, and when plan is confirmed.
- [ ] **TASK-312** `[BE-Services]` **PDF Export Service (WeasyPrint / ReportLab)**
  - **Feature**: #34
  - **Target Files**: `backend/app/api/v1/export.py`, `backend/app/services/export_service.py`
  - **Acceptance Criteria**: `GET /events/{id}/export/pdf` generates downloadable PDF with event timeline, stop details, map snapshot, and expense summary.
- [ ] **TASK-313** `[BE-Services]` **Packing Checklist Generation Service**
  - **Feature**: #35
  - **Target Files**: `backend/app/services/checklist_service.py`
  - **Acceptance Criteria**: Generates customizable packing list based on EventType and weather forecast.

### 3.4 Plan, Voting & Checklist UI Screens (Frontend Core & Growth)
- [ ] **TASK-314** `[FE-A]` **Manual Plan Builder Component (Drag & Drop)**
  - **Feature**: #11, #12
  - **Target Files**: `frontend/src/features/plan/components/PlanBuilder.tsx`
  - **Acceptance Criteria**: Allows adding stops with Google Places autocomplete, reordering stops via drag & drop, editing cost/notes.
- [ ] **TASK-315** `[FE-A]` **Voting Dashboard & Comment Thread UI**
  - **Feature**: #13
  - **Target Files**: `frontend/src/features/plan/components/PlanVotingCard.tsx`
  - **Acceptance Criteria**: Displays UP/DOWN/NEUTRAL buttons, vote count progress bar, comment thread, "Send for Vote" button.
- [ ] **TASK-316** `[FE-A]` **Plan Confirmation & Status Badge UI**
  - **Feature**: #14
  - **Target Files**: `frontend/src/features/plan/components/PlanHeader.tsx`
  - **Acceptance Criteria**: Shows status badge (Draft, Voting, Confirmed). Renders "Confirm Plan" button only for Event Owner.
- [ ] **TASK-317** `[FE-B]` **Packing Checklist UI Screen**
  - **Feature**: #35
  - **Target Files**: `frontend/src/features/checklist/pages/ChecklistPage.tsx`
  - **Acceptance Criteria**: Interactive checklist with item check/uncheck, custom item add/delete, progress bar.

---

## 🚀 Sprint 4 — Realtime AI Chat, Admin Dashboard & Pentest

### 4.1 Realtime AI Chat Engine (AI & Backend Integration)
- [ ] **TASK-401** `[AI]` **Chat Agent & Function Calling Setup**
  - **Feature**: #31
  - **Target Files**: `backend/app/ai_agents/agents/chat_agent.py`
  - **Acceptance Criteria**: Chat Agent routes user queries, calls sub-agent tools dynamically, maintains conversation state.
- [ ] **TASK-402** `[AI]` **FastAPI WebSocket & SSE Endpoints for Streaming**
  - **Feature**: #31
  - **Target Files**: `backend/app/api/v1/ai.py`
  - **Acceptance Criteria**: `/api/v1/ai/chat/stream` streams LLM output tokens in real-time using `EventSourceResponse` (SSE) or WebSockets.
- [ ] **TASK-403** `[AI]` **Agent Token Logging Service**
  - **Feature**: #36
  - **Target Files**: `backend/app/services/agent_logger.py`
  - **Acceptance Criteria**: Every LLM call logs `input_tokens`, `output_tokens`, `duration_ms`, `agent_name`, `user_id` to `agent_logs` table.

### 4.2 Shared Expense Splitting & Settlement (Backend Services)
- [ ] **TASK-404** `[BE-Services]` **Expense Splitting & Optimal Settlement Algorithm**
  - **Feature**: #41
  - **Target Files**: `backend/app/services/expense_service.py`, `backend/app/services/settlement_service.py`
  - **Acceptance Criteria**: Tính split theo 3 kiểu `SplitType` — `EQUAL`, `EXACT`, `PERCENTAGE`; tính net balance từng member bằng SQL GROUP BY (không cần bảng `MemberBalance`, theo [database-schema.md](../03-architecture/database-schema.md) §3). `SettlementService.settle()` chạy **thuật toán tối ưu số giao dịch** theo ví dụ §3 (A/B/C/D → 3 transactions) — thuật toán greedy: tạo biểu đồ creditor/debtor từ net balance, khớp cặp, số transaction ≤ số người nợ; lưu từng giao dịch bù trừ vào bảng `settlements` (1 dòng `Settlement`, `isSettled=false`). Unit test thuật toán trên cases 2/3/4 người (định nghĩa trong `tests/test_settlement.py`).
- [ ] **TASK-415** `[BE-Services]` **Fund & Expense CRUD + Settlement Persistence APIs**
  - **Feature**: #41
  - **Target Files**: `backend/app/api/v1/funds.py` (router thu quỹ — tạo `Expense(type=ADVANCE)`, không có bảng/model riêng), `backend/app/api/v1/expenses.py`, `backend/app/api/v1/settlements.py`, `backend/app/models/expense.py`, `backend/app/models/settlement.py`
  - **Acceptance Criteria**: `POST/GET/PATCH/DELETE /events/{id}/fund-contributions` (thu quỹ → tạo `Expense(type=ADVANCE)`) và `/events/{id}/expenses` (mỗi expense tạo `expense_splits` theo SplitType); `GET /events/{id}/balances` trả net balance từng member (SQL GROUP BY); `GET /events/{id}/settlements` + `POST /events/{id}/settlements` (chạy thuật toán TASK-404, ghi bảng `settlements`). Role guard: chỉ OWNER/MEMBER được sửa expense (theo RolesGuard TASK-204). Alembic migration + tests `test_expense.py`, `test_settlement.py`.

### 4.3 Admin Dashboard Service (Backend Services)
- [ ] **TASK-405** `[BE-Services]` **Admin Statistics APIs**
  - **Feature**: #36, #37
  - **Target Files**: `backend/app/api/v1/admin.py`, `backend/app/services/admin_service.py`
  - **Acceptance Criteria**: `GET /admin/dashboard/overview` returns total users, total events, token usage history, cache hit rate. `GET /admin/users` lists and manages user status.

### 4.4 AI Experience, Shared Expenses & Admin UI (Frontend Growth)
- [ ] **TASK-406** `[FE-B]` **AI Chat Interface with Streaming Output**
  - **Feature**: #31, #32
  - **Target Files**: `frontend/src/features/ai-chat/pages/ChatPage.tsx`
  - **Acceptance Criteria**: Chat interface renders streaming response, user typing indicator, suggestion quick-chips.
- [ ] **TASK-407** `[FE-B]` **Interactive Draft Plan Card Renderer**
  - **Feature**: #32
  - **Target Files**: `frontend/src/features/ai-chat/components/PlanCardPreview.tsx`
  - **Acceptance Criteria**: Renders AI proposal inside chat as structured card with "Accept as Draft" or "Modify" buttons.
- [ ] **TASK-408** `[FE-B]` **Category-Specific Stop Cards Rendering**
  - **Feature**: #25, #32
  - **Target Files**: `frontend/src/features/plan/components/StopCategoryCard.tsx`
  - **Acceptance Criteria**: Custom card designs: displays menu items for RESTAURANT, activity ticket prices for ENTERTAINMENT, opening hours/tips for SIGHTSEEING.
- [ ] **TASK-409** `[FE-B]` **Shared Expense & Settlement UI**
  - **Feature**: #41
  - **Target Files**: `frontend/src/features/expense/pages/ExpensePage.tsx`, `frontend/src/features/expense/components/ExpenseForm.tsx`, `frontend/src/features/expense/components/FundPoolCard.tsx`, `frontend/src/features/expense/components/SettlementTable.tsx`
  - **Acceptance Criteria**: UI tương ứng API TASK-415: form thêm expense chọn SplitType (EQUAL/EXACT/PERCENTAGE), hiển thị fund pool + từng member đóng bao nhiêu, danh sách expense, net balance từng người, bảng settlement tối ưu (ai trả ai bao nhiêu) kèm trạng thái settled toggle. Empty/loading/error states đầy đủ (theo wireframe TASK-010).
- [ ] **TASK-410** `[FE-B]` **Admin Dashboard UI Screen**
  - **Feature**: #36, #37
  - **Target Files**: `frontend/src/features/admin/pages/AdminDashboardPage.tsx`
  - **Acceptance Criteria**: Renders token cost charts (Recharts), active user stats, API usage breakdown, user table.

### 4.5 Security Hardening & Pentest
- [ ] **TASK-411** `[SEC/DEVOPS]` **Input Sanitization & Boundary Validation Audit**
  - **Feature**: Security
  - **Target Files**: `backend/app/ai_agents/`, `backend/app/schemas/`
  - **Acceptance Criteria**: Verifies all user inputs are sanitized (Pydantic & bleach); checks system/user/assistant message roles framing without raw string concatenation.
- [ ] **TASK-412** `[SEC/DEVOPS]` **Pydantic Output Validation Audit**
  - **Feature**: Security
  - **Target Files**: `backend/app/ai_agents/llm_provider.py`
  - **Acceptance Criteria**: Ensures unparseable or malicious LLM outputs trigger graceful fallback without server crash or raw output leakage.
- [ ] **TASK-413** `[SEC/DEVOPS]` **OWASP Top 10 Security Pentest**
  - **Feature**: Security
  - **Target Files**: Entire Application
  - **Acceptance Criteria**: Verifies SQL injection safety (SQLAlchemy parameterized queries), XSS escaping, CORS enforcement, and authorization guards across all endpoints.
- [ ] **TASK-414** `[SEC/DEVOPS]` **Production Build & Deployment Validation (Vercel + Render)**
  - **Feature**: DevOps
  - **Target Files**: `docker-compose.prod.yml`, `vercel.json`, `render.yaml`, GitHub Actions
  - **Acceptance Criteria**: Production Docker container builds cleanly; **end-to-end smoke test trên URL production thật** — Frontend tại Vercel domain (từ TASK-118) gọi Backend tại Render domain (từ TASK-216): đăng nhập → tạo event → tạo plan → xem expense, `/health` green, SSL + CORS đúng domain, environment secrets không lộ (quét `.env`/hardcoded key). Có checklist verify trước khi demo cuối.
