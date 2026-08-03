# 👤 Person 2 — Backend Dev B (Platform & Integration)

> **Sở hữu**: External API/Cache (N3) + Notification/Export (N5) + Admin (N6).
> **Tham gia bắt buộc**: Contract Session (Sprint 0), Integration Day cuối mỗi Sprint.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 0 Tasks (Support Contract Session) | 0/0 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | 0/2 | 🔲 To Do |
| **Sprint 2** | 4 Tasks | 0/4 | 🔲 To Do |
| **Sprint 3** | 3 Tasks | 0/3 | 🔲 To Do |
| **Sprint 4** | 1 Task | 0/1 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 1 — Platform & External Integration Baseline
- [ ] **`TASK-107`** **HTTPX Async Client & Redis Caching Service**
  - **Feature**: #22
  - **Target Files**: `backend/app/core/redis.py`, `backend/app/services/cache_service.py`
  - **Acceptance Criteria**: Generic cache decorator `cache_response(ttl=3600)` stores and retrieves JSON responses from Redis.
- [ ] **`TASK-108`** **Google Places API Base Service**
  - **Feature**: #17
  - **Target Files**: `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `PlacesService.search_places()` queries Google Places API using `httpx.AsyncClient` and caches in Redis.

### Sprint 2 — External Integrations & Places Filtering
- [ ] **`TASK-205`** **Google Places Search with Category Filter**
  - **Feature**: #17
  - **Target Files**: `backend/app/api/v1/places.py`, `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `GET /api/v1/places/search?category=RESTAURANT|CAFE|ENTERTAINMENT|ATTRACTION` filters Google Places API response and attaches category metadata.
- [ ] **`TASK-206`** **Hotel Data Comparison Service**
  - **Feature**: #18
  - **Target Files**: `backend/app/api/v1/places.py`, `backend/app/services/hotel_service.py`
  - **Acceptance Criteria**: `GET /api/v1/hotels/compare?ids=...` compares price, rating, amenities of hotels side-by-side.
- [ ] **`TASK-207`** **OpenWeatherMap Integration Service**
  - **Feature**: #20
  - **Target Files**: `backend/app/api/v1/utils.py`, `backend/app/services/weather_service.py`
  - **Acceptance Criteria**: `GET /api/v1/weather?lat=&lng=` returns forecast, temperature, weather conditions. Cached for 3 hours.
- [ ] **`TASK-208`** **Currency Converter API**
  - **Feature**: #21
  - **Target Files**: `backend/app/api/v1/utils.py`, `backend/app/services/currency_service.py`
  - **Acceptance Criteria**: `GET /api/v1/exchange-rate?from=USD&to=VND` fetches live exchange rates with 12h Redis cache.

### Sprint 3 — Notifications & Export PDF
- [ ] **`TASK-311`** **Email Notification Service (SMTP)**
  - **Feature**: #33
  - **Target Files**: `backend/app/services/notification_service.py`
  - **Acceptance Criteria**: Sends email notifications when invited to event, when plan vote opens, and when plan is confirmed.
- [ ] **`TASK-312`** **PDF Export Service (WeasyPrint / ReportLab)**
  - **Feature**: #34
  - **Target Files**: `backend/app/api/v1/export.py`, `backend/app/services/export_service.py`
  - **Acceptance Criteria**: `GET /events/:id/export/pdf` generates downloadable PDF with event timeline, stop details, map snapshot, and expense summary.
- [ ] **`TASK-313`** **Packing Checklist Generation Service**
  - **Feature**: #35
  - **Target Files**: `backend/app/services/checklist_service.py`
  - **Acceptance Criteria**: Generates customizable packing list based on EventType and weather forecast.

### Sprint 4 — Admin Dashboard APIs
- [ ] **`TASK-405`** **Admin Statistics APIs**
  - **Feature**: #36, #37
  - **Target Files**: `backend/app/api/v1/admin.py`, `backend/app/services/admin_service.py`
  - **Acceptance Criteria**: `GET /admin/dashboard/overview` returns total users, total events, token usage history, cache hit rate. `GET /admin/users` lists and manages user status.

---

## 🤝 Handover & Review Guidelines (Person 2)

1. **Buddy / Backup**: `Person 1` (Backend Dev A)
2. **Task Completion**: Run `pytest backend/tests/test_places.py` and `ruff check backend`. Push branch `feature/TASK-xxx` and tag `@BE-A` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
