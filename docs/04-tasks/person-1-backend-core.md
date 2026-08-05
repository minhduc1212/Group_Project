# 👤 Person 1 — Tạ Quang Huy (Backend Dev A: Core Domain & AI Integration)

> **Người phụ trách**: **Tạ Quang Huy**
> **Sở hữu**: Auth (N1) + Event/Plan/Vote/Invitation (N2) — người thiết kế DB schema & FastAPI models gốc dùng chung toàn hệ thống + Kiêm nhiệm AI Agent Integration (Tool Calling & Data Bridge).
> **Tham gia bắt buộc**: Contract Session (Sprint 0), Integration Day cuối mỗi Sprint.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 2 Tasks | 0/2 | 🔲 To Do |
| **Sprint 1** | 6 Tasks | 0/6 | 🔲 To Do |
| **Sprint 2** | 4 Tasks | 0/4 | 🔲 To Do |
| **Sprint 3** | 6 Tasks | 0/6 | 🔲 To Do |
| **Sprint 4** | 1 Task | 0/1 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — Contract Session
- [ ] **`TASK-001`** **Design SQLAlchemy & Pydantic DB Schemas**
  - **Feature**: N/A (Sprint 0 Contract)
  - **Target Files**: `backend/app/models/` (`user.py`, `event.py`, `plan.py`, `vote.py`, `invitation.py`, `log.py`), `backend/app/schemas/`
  - **Acceptance Criteria**: Full support for `EventType`, `StopCategory`, `metadata` JSON, `Invitation`, `PlanStatus`. Migration passes clean via Alembic.
- [ ] **`TASK-002`** **FastAPI APIRouter Skeleton**
  - **Feature**: N/A (Contract)
  - **Target Files**: `backend/app/api/v1/` (`auth.py`, `events.py`, `plans.py`, `votes.py`, `invitations.py`)
  - **Acceptance Criteria**: Routes return `501 Not Implemented` with matching Pydantic response models. Swagger accessible at `/docs`.

### Sprint 1 — Auth & User Management (FastAPI + PyJWT)
- [ ] **`TASK-101`** **Database Models & Alembic Initial Migration**
  - **Feature**: #2, #4
  - **Target Files**: `backend/app/models/user.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: User table created with `id`, `email`, `password_hash`, `full_name`, `avatar_url`, `provider`.
- [ ] **`TASK-102`** **User Registration & Password Hashing**
  - **Feature**: #2
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/services/auth_service.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/register` validates Pydantic schema, hashes password using `passlib[bcrypt]`, returns user JWT tokens.
- [ ] **`TASK-103`** **OAuth2 Integration (Google & Facebook)**
  - **Feature**: #1
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/core/oauth.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/login/google` exchanges auth code for token, creates or logs in user, returns JWT access/refresh token.
- [ ] **`TASK-104`** **JWT Access & Refresh Token Rotation**
  - **Feature**: #5
  - **Target Files**: `backend/app/core/security.py`, `backend/app/api/v1/auth.py`
  - **Acceptance Criteria**: Access token expires in 15 mins. `POST /api/v1/auth/refresh-token` validates refresh token in httpOnly cookie and issues new pair.
- [ ] **`TASK-105`** **Forgot & Reset Password Flow**
  - **Feature**: #3
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/services/email_service.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/forgot-password` generates single-use 15-min token and sends email via SMTP.
- [ ] **`TASK-106`** **User Profile API (GET & PATCH)**
  - **Feature**: #4
  - **Target Files**: `backend/app/api/v1/users.py`, `backend/app/services/user_service.py`
  - **Acceptance Criteria**: `GET /api/v1/users/me` returns current user profile; `PATCH /api/v1/users/me` updates `full_name`, `avatar_url`.

### Sprint 2 — Event, Plan & Invitation Management
- [ ] **`TASK-201`** **Event Database Models & Alembic Migration**
  - **Feature**: #6
  - **Target Files**: `backend/app/models/event.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: Tables `events` and `event_members` created with `EventType` enum and `EventRole` enum.
- [ ] **`TASK-202`** **Event CRUD APIs**
  - **Feature**: #6, #9
  - **Target Files**: `backend/app/api/v1/events.py`, `backend/app/services/event_service.py`
  - **Acceptance Criteria**: `POST /events` creates event and assigns creator as `OWNER`. `GET /events` lists user events. `PATCH /events/:id` updates event info.
- [ ] **`TASK-203`** **Invitation Database Model & APIs**
  - **Feature**: #7
  - **Target Files**: `backend/app/models/invitation.py`, `backend/app/api/v1/invitations.py`
  - **Acceptance Criteria**: `POST /events/:id/invitations` generates invitation. `PATCH /invitations/:id` allows user to ACCEPT or DECLINE.
- [ ] **`TASK-204`** **RolesGuard Dependency (Owner / Member / Viewer)**
  - **Feature**: #8
  - **Target Files**: `backend/app/api/v1/dependencies.py`
  - **Acceptance Criteria**: Reusable FastAPI dependency `require_role(min_role)` raises `403 Forbidden` if user lacks permissions.

### Sprint 3 — Voting System, Manual Plan & Metadata
- [ ] **`TASK-301`** **Plan & PlanStop Models with Category Metadata**
  - **Feature**: #10, #11, #12
  - **Target Files**: `backend/app/models/plan.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: Tables `plans`, `plan_stops`, `plan_votes` created with `created_by_id`, `is_ai_generated`, `PlanStatus` enum, `StopCategory` enum, `metadata` JSON.
- [ ] **`TASK-302`** **Manual Plan Creation API**
  - **Feature**: #11
  - **Target Files**: `backend/app/api/v1/plans.py`, `backend/app/services/plan_service.py`
  - **Acceptance Criteria**: `POST /events/:id/plans` with `is_ai_generated=False` creates manual plan with initial status `DRAFT`.
- [ ] **`TASK-303`** **Plan Stop Management API (Reorder / Add / Delete / Edit)**
  - **Feature**: #12
  - **Target Files**: `backend/app/api/v1/plans.py`
  - **Acceptance Criteria**: `PATCH /events/:id/plans/:planId/stops` supports reordering stop sequence, updating notes, cost, and JSON metadata.
- [ ] **`TASK-304`** **Plan Vote API & Tallying Logic**
  - **Feature**: #13
  - **Target Files**: `backend/app/api/v1/votes.py`, `backend/app/services/vote_service.py`
  - **Acceptance Criteria**: `POST /events/:id/plans/:planId/votes` allows voting UP, DOWN, NEUTRAL with optional comment. Enforces unique constraint per `(plan_id, user_id)`.
- [ ] **`TASK-305`** **Plan Status Transition API (DRAFT → VOTING → CONFIRMED)**
  - **Feature**: #14
  - **Target Files**: `backend/app/api/v1/plans.py`
  - **Acceptance Criteria**: Creator can set `VOTING`. Only `OWNER` can confirm plan (`CONFIRMED`). Updates plan status and locks confirmed version.
- [ ] **`TASK-306`** **Saved Places API**
  - **Feature**: #15
  - **Target Files**: `backend/app/api/v1/saved_places.py`
  - **Acceptance Criteria**: `POST /saved-places` saves favorite restaurant, place, or venue to user's saved list.

### Sprint 4 — Shared Expense Calculation & Hardening
- [ ] **`TASK-404`** **Expense Splitting Calculation Service**
  - **Feature**: #41
  - **Target Files**: `backend/app/services/expense_service.py`
  - **Acceptance Criteria**: Computes equal per-person split, custom itemized split, and balance summary for event members.

---

## 🤝 Handover & Review Guidelines (Person 1)

1. **Buddy / Backup**: `Person 2` (Backend Dev B)
2. **Task Completion**: Run `pytest backend/tests/test_auth.py` and `ruff check backend`. Push branch `feature/TASK-xxx` and tag `@BE-B` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
