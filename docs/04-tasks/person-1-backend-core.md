# 👤 Person 1 — Tạ Quang Huy (Backend Dev A: Core Domain & AI Integration)

> **Người phụ trách**: **Tạ Quang Huy**
> **Sở hữu**: Event/Plan/Vote (N2) — người thiết kế DB schema & FastAPI models gốc dùng chung (Auth chỉ giữ DB model 101) + Kiêm nhiệm AI Agent Integration (Tool Calling & Data Bridge).
> **Tham gia bắt buộc**: Contract Session (Sprint 0), Integration Day cuối mỗi Sprint.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 1 Task | 0/1 | 🔲 To Do |
| **Sprint 1** | 1 Task | 0/1 | 🔲 To Do |
| **Sprint 2** | 3 Tasks | 0/3 | 🔲 To Do |
| **Sprint 3** | 6 Tasks | 0/6 | 🔲 To Do |
| **Sprint 4** | 0 Tasks (Review AI Integration & Expense/Settlement) | 0/0 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — Contract Session
- [ ] **`TASK-001`** **Design SQLAlchemy & Pydantic DB Schemas**
  - **Feature**: N/A (Sprint 0 Contract)
  - **Target Files**: `backend/app/models/` (`user.py`, `event.py`, `plan.py`, `vote.py`, `invitation.py`, `log.py`, **`fund.py`, `expense.py`, `settlement.py`**), `backend/app/schemas/`
  - **Acceptance Criteria**: Full support for `EventType`, `StopCategory`, `metadata` JSON, `Invitation`, `PlanStatus`. Có đủ 6 bảng tài chính trong [database-schema.md](../03-architecture/database-schema.md): `fund_contributions`, `expenses`, `expense_splits`, `event_settlements`, `member_balances`, `settlement_transactions` + `total_budget`/`estimated_cost` trên Plan. Migration passes clean via Alembic.
### Sprint 1 — Core DB Models & Migration
> Auth APIs (102–106) đã chuyển sang Person 2 (Phạm Đình Ánh Dương).
- [ ] **`TASK-101`** **Database Models & Alembic Initial Migration**
  - **Feature**: #2, #4
  - **Target Files**: `backend/app/models/user.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: User table created with `id`, `email`, `password_hash`, `full_name`, `avatar_url`, `provider`.

### Sprint 2 — Event & Plan Management
- [ ] **`TASK-201`** **Event Database Models & Alembic Migration**
  - **Feature**: #6
  - **Target Files**: `backend/app/models/event.py`, `backend/alembic/versions/`
  - **Acceptance Criteria**: Tables `events` and `event_members` created with `EventType` enum and `EventRole` enum.
- [ ] **`TASK-202`** **Event CRUD APIs**
  - **Feature**: #6, #9
  - **Target Files**: `backend/app/api/v1/events.py`, `backend/app/services/event_service.py`
  - **Acceptance Criteria**: `POST /events` creates event and assigns creator as `OWNER`. `GET /events` lists user events. `PATCH /events/{id}` updates event info.
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
  - **Acceptance Criteria**: `POST /events/{id}/plans` with `is_ai_generated=False` creates manual plan with initial status `DRAFT`.
- [ ] **`TASK-303`** **Plan Stop Management API (Reorder / Add / Delete / Edit)**
  - **Feature**: #12
  - **Target Files**: `backend/app/api/v1/plans.py`
  - **Acceptance Criteria**: `PATCH /events/{id}/plans/{planId}/stops` supports reordering stop sequence, updating notes, cost, and JSON metadata.
- [ ] **`TASK-304`** **Plan Vote API & Tallying Logic**
  - **Feature**: #13
  - **Target Files**: `backend/app/api/v1/votes.py`, `backend/app/services/vote_service.py`
  - **Acceptance Criteria**: `POST /events/{id}/plans/{planId}/votes` allows voting UP, DOWN, NEUTRAL with optional comment. Enforces unique constraint per `(plan_id, user_id)`.
- [ ] **`TASK-305`** **Plan Status Transition API (DRAFT → VOTING → CONFIRMED)**
  - **Feature**: #14
  - **Target Files**: `backend/app/api/v1/plans.py`
  - **Acceptance Criteria**: Creator can set `VOTING`. Only `OWNER` can confirm plan (`CONFIRMED`). Updates plan status and locks confirmed version.
- [ ] **`TASK-306`** **Saved Places API**
  - **Feature**: #15
  - **Target Files**: `backend/app/api/v1/saved_places.py`
  - **Acceptance Criteria**: `POST /saved-places` saves favorite restaurant, place, or venue to user's saved list.

### Sprint 4 — AI Integration (Review)
- **TASK-404** (Expense Splitting & Optimal Settlement Algorithm) + **TASK-415** (Fund & Expense CRUD) → đã chuyển sang [person-2-backend-platform.md](person-2-backend-platform.md) — **Phạm Đình Ánh Dương** (Sprint 4).
- **AI Integration** của Tạ Quang Huy: TASK-402 (FastAPI WebSocket/SSE) + TASK-403 (Agent Token Logging) — theo dõi chi tiết tại [person-3-ai-engineer.md](person-3-ai-engineer.md) (Sprint 4).
- Person 1 đảm nhận vai trò **reviewer** cho cụm Expense/Settlement (404/415) và AI Integration (402/403).

---

## 🤝 Handover & Review Guidelines (Person 1)

1. **Buddy / Backup**: `Person 2` (Backend Dev B)
2. **Task Completion**: Run `pytest backend/tests/test_auth.py` and `ruff check backend`. Push branch `feature/TASK-xxx` and tag `@BE-B` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
