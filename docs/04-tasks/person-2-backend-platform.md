# 👤 Person 2 — Hà Đăng Huy & Phạm Đình Ánh Dương (Backend Dev B: Platform, Services & Integration)

> **Người phụ trách**: 
> - **Hà Đăng Huy** (Backend Dev B: External API/Cache N3 + Places, Weather, Currency + Kiêm Frontend Core UI)
> - **Phạm Đình Ánh Dương** (Backend Dev C: Auth & User APIs N1, Notification/Export N5 + Invitations, Forgot/Reset Email, Expense Splitting & Settlement + Admin APIs N6)
> **Tham gia bắt buộc**: Contract Session (Sprint 0), Integration Day cuối mỗi Sprint.

---

## 📊 Progress Tracker

| Sprint | Task Count | Người phụ trách | Done | Status |
|---|---|---|---|---|
| **Sprint 0** | 1 Task | Phạm Đình Ánh Dương | 0/1 | 🔲 To Do |
| **Sprint 1** | 7 Tasks | Hà Đăng Huy (2) + Phạm Đình Ánh Dương (5) | 0/7 | 🔲 To Do |
| **Sprint 2** | 5 Tasks | Hà Đăng Huy (4) + Phạm Đình Ánh Dương (1) | 0/5 | 🔲 To Do |
| **Sprint 3** | 3 Tasks | Phạm Đình Ánh Dương | 0/3 | 🔲 To Do |
| **Sprint 4** | 3 Tasks | Phạm Đình Ánh Dương | 0/3 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — Contract Session (Phụ trách: Phạm Đình Ánh Dương)
- [ ] **`TASK-002`** `[BE-Services - Phạm Đình Ánh Dương]` **FastAPI APIRouter Skeleton**
  - **Feature**: N/A (Contract)
  - **Target Files**: `backend/app/api/v1/` (`auth.py`, `events.py`, `plans.py`, `votes.py`, `invitations.py`)
  - **Acceptance Criteria**: Routes return `501 Not Implemented` with matching Pydantic response models. Swagger accessible at `/docs`.

### Sprint 1 — Auth APIs, Platform & External Integration Baseline (Phụ trách: Hà Đăng Huy & Phạm Đình Ánh Dương)
- [ ] **`TASK-107`** `[BE-Platform - Hà Đăng Huy]` **HTTPX Async Client & Redis Caching Service**
  - **Feature**: #22
  - **Target Files**: `backend/app/core/redis.py`, `backend/app/services/cache_service.py`
  - **Acceptance Criteria**: Generic cache decorator `cache_response(ttl=3600)` stores and retrieves JSON responses from Redis.
- [ ] **`TASK-108`** `[BE-Platform - Hà Đăng Huy]` **Google Places API Base Service**
  - **Feature**: #17
  - **Target Files**: `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `PlacesService.search_places()` queries Google Places API using `httpx.AsyncClient` and caches in Redis.
- [ ] **`TASK-105`** `[BE-Services - Phạm Đình Ánh Dương]` **Forgot & Reset Password Flow**
  - **Feature**: #3
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/services/email_service.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/forgot-password` generates single-use 15-min token and sends email via SMTP.
- [ ] **`TASK-102`** `[BE-Services - Phạm Đình Ánh Dương]` **User Registration & Password Hashing**
  - **Feature**: #2
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/services/auth_service.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/register` validates Pydantic schema, hashes password using `passlib[bcrypt]`, returns user JWT tokens.
- [ ] **`TASK-103`** `[BE-Services - Phạm Đình Ánh Dương]` **OAuth2 Integration (Google & Facebook)**
  - **Feature**: #1
  - **Target Files**: `backend/app/api/v1/auth.py`, `backend/app/core/oauth.py`
  - **Acceptance Criteria**: `POST /api/v1/auth/login/google` exchanges auth code for token, creates or logs in user, returns JWT access/refresh token.
- [ ] **`TASK-104`** `[BE-Services - Phạm Đình Ánh Dương]` **JWT Access & Refresh Token Rotation**
  - **Feature**: #5
  - **Target Files**: `backend/app/core/security.py`, `backend/app/api/v1/auth.py`
  - **Acceptance Criteria**: Access token expires in 15 mins. `POST /api/v1/auth/refresh-token` validates refresh token in httpOnly cookie and issues new pair.
- [ ] **`TASK-106`** `[BE-Services - Phạm Đình Ánh Dương]` **User Profile API (GET & PATCH)**
  - **Feature**: #4
  - **Target Files**: `backend/app/api/v1/users.py`, `backend/app/services/user_service.py`
  - **Acceptance Criteria**: `GET /api/v1/users/me` returns current user profile; `PATCH /api/v1/users/me` updates `full_name`, `avatar_url`.

### Sprint 2 — External Integrations & Places Filtering (Phụ trách: Hà Đăng Huy)
- [ ] **`TASK-205`** `[BE-Platform - Hà Đăng Huy]` **Google Places Search with Category Filter**
  - **Feature**: #17
  - **Target Files**: `backend/app/api/v1/places.py`, `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `GET /api/v1/places/search?category=RESTAURANT|CAFE|ENTERTAINMENT|ATTRACTION` filters Google Places API response and attaches category metadata.
- [ ] **`TASK-206`** `[BE-Platform - Hà Đăng Huy]` **Hotel Data Comparison Service**
  - **Feature**: #18
  - **Target Files**: `backend/app/api/v1/places.py`, `backend/app/services/hotel_service.py`
  - **Acceptance Criteria**: `GET /api/v1/hotels/compare?ids=...` compares price, rating, amenities of hotels side-by-side.
- [ ] **`TASK-207`** `[BE-Platform - Hà Đăng Huy]` **OpenWeatherMap Integration Service**
  - **Feature**: #20
  - **Target Files**: `backend/app/api/v1/utils.py`, `backend/app/services/weather_service.py`
  - **Acceptance Criteria**: `GET /api/v1/weather?lat=&lng=` returns forecast, temperature, weather conditions. Cached for 3 hours.
- [ ] **`TASK-208`** `[BE-Platform - Hà Đăng Huy]` **Currency Converter API**
  - **Feature**: #21
  - **Target Files**: `backend/app/api/v1/utils.py`, `backend/app/services/currency_service.py`
  - **Acceptance Criteria**: `GET /api/v1/exchange-rate?from=USD&to=VND` fetches live exchange rates with 12h Redis cache.
- [ ] **`TASK-203`** `[BE-Services - Phạm Đình Ánh Dương]` **Invitation Database Model & APIs**
  - **Feature**: #7
  - **Target Files**: `backend/app/models/invitation.py`, `backend/app/api/v1/invitations.py`
  - **Acceptance Criteria**: `POST /events/{id}/invitations` generates invitation. `PATCH /invitations/{id}` allows user to ACCEPT or DECLINE.

### Sprint 3 — Notifications, PDF Export & Realtime (Phụ trách: Phạm Đình Ánh Dương)
- [ ] **`TASK-311`** `[BE-Services - Phạm Đình Ánh Dương]` **Email Notification Service (SMTP)**
  - **Feature**: #33
  - **Target Files**: `backend/app/services/notification_service.py`
  - **Acceptance Criteria**: Sends email notifications when invited to event, when plan vote opens, and when plan is confirmed.
- [ ] **`TASK-312`** `[BE-Services - Phạm Đình Ánh Dương]` **PDF Export Service (WeasyPrint / ReportLab)**
  - **Feature**: #34
  - **Target Files**: `backend/app/api/v1/export.py`, `backend/app/services/export_service.py`
  - **Acceptance Criteria**: `GET /events/{id}/export/pdf` generates downloadable PDF with event timeline, stop details, map snapshot, and expense summary.
- [ ] **`TASK-313`** `[BE-Services - Phạm Đình Ánh Dương]` **Packing Checklist Generation Service**
  - **Feature**: #35
  - **Target Files**: `backend/app/services/checklist_service.py`
  - **Acceptance Criteria**: Generates customizable packing list based on EventType and weather forecast.

### Sprint 4 — Admin Dashboard, Expense Splitting & Settlement (Phụ trách: Phạm Đình Ánh Dương)
- [ ] **`TASK-405`** `[BE-Services - Phạm Đình Ánh Dương]` **Admin Statistics & Realtime APIs**
  - **Feature**: #36, #37
  - **Target Files**: `backend/app/api/v1/admin.py`, `backend/app/services/admin_service.py`
  - **Acceptance Criteria**: `GET /admin/dashboard/overview` returns total users, total events, token usage history, cache hit rate. `GET /admin/users` lists and manages user status.
- [ ] **`TASK-404`** `[BE-Services - Phạm Đình Ánh Dương]` **Expense Splitting & Optimal Settlement Algorithm**
  - **Feature**: #41
  - **Target Files**: `backend/app/services/expense_service.py`, `backend/app/services/settlement_service.py`
  - **Acceptance Criteria**: Tính split theo 3 kiểu `SplitType` — `EQUAL`, `EXACT`, `PERCENTAGE`; tính net balance từng member bằng SQL GROUP BY (không cần bảng `MemberBalance`, theo [database-schema.md](../03-architecture/database-schema.md) §3). `SettlementService.settle()` chạy thuật toán tối ưu số giao dịch theo ví dụ §3 (A/B/C/D → 3 transactions); lưu từng giao dịch bù trừ vào bảng `settlements` (1 dòng `Settlement`, `isSettled=false`). Unit test trong `tests/test_settlement.py` (cases 2/3/4 người).
- [ ] **`TASK-415`** `[BE-Services - Phạm Đình Ánh Dương]` **Fund & Expense CRUD + Settlement Persistence APIs**
  - **Feature**: #41
  - **Target Files**: `backend/app/api/v1/funds.py`, `backend/app/api/v1/expenses.py`, `backend/app/api/v1/settlements.py`, `backend/app/models/fund.py`, `backend/app/models/expense.py`, `backend/app/models/settlement.py`
  - **Acceptance Criteria**: `POST/GET/PATCH/DELETE /events/{id}/fund-contributions` và `/events/{id}/expenses` (mỗi expense tạo `expense_splits` theo SplitType); `GET /events/{id}/balances` trả net balance từng member; `GET/POST /events/{id}/settlements` (chạy thuật toán TASK-404, ghi `EventSettlement`). Role guard theo RolesGuard TASK-204. Alembic migration + tests `test_expense.py`, `test_settlement.py`.

---

## 🤝 Handover & Review Guidelines (Person 2)

1. **Buddy / Backup**: **Tạ Quang Huy** (Backend Dev A)
2. **Task Completion**: Run `pytest backend/tests/test_places.py` and `ruff check backend`. Push branch `feature/TASK-xxx` and tag `@BE-Core` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
