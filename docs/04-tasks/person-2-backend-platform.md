# 👤 Person 2 — Hà Đăng Huy & Phạm Đình Ánh Dương (Backend Dev B: Platform, Services & Integration)

> **Người phụ trách**: 
> - **Hà Đăng Huy** (Backend Dev B: External API/Cache N3 + Places, Weather, Currency + Kiêm Frontend Core UI)
> - **Phạm Đình Ánh Dương** (Backend Dev C: Notification/Export N5 + Realtime SSE/WS + Admin APIs N6)
> **Tham gia bắt buộc**: Contract Session (Sprint 0), Integration Day cuối mỗi Sprint.

---

## 📊 Progress Tracker

| Sprint | Task Count | Người phụ trách | Done | Status |
|---|---|---|---|---|
| **Sprint 0** | 0 Tasks | Hà Đăng Huy & Phạm Đình Ánh Dương | 0/0 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | Hà Đăng Huy | 0/2 | 🔲 To Do |
| **Sprint 2** | 4 Tasks | Hà Đăng Huy | 0/4 | 🔲 To Do |
| **Sprint 3** | 3 Tasks | Phạm Đình Ánh Dương | 0/3 | 🔲 To Do |
| **Sprint 4** | 1 Task | Phạm Đình Ánh Dương | 0/1 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 1 — Platform & External Integration Baseline (Phụ trách: Hà Đăng Huy)
- [ ] **`TASK-107`** `[BE-Platform - Hà Đăng Huy]` **HTTPX Async Client & Redis Caching Service**
  - **Feature**: #22
  - **Target Files**: `backend/app/core/redis.py`, `backend/app/services/cache_service.py`
  - **Acceptance Criteria**: Generic cache decorator `cache_response(ttl=3600)` stores and retrieves JSON responses from Redis.
- [ ] **`TASK-108`** `[BE-Platform - Hà Đăng Huy]` **Google Places API Base Service**
  - **Feature**: #17
  - **Target Files**: `backend/app/services/places_service.py`
  - **Acceptance Criteria**: `PlacesService.search_places()` queries Google Places API using `httpx.AsyncClient` and caches in Redis.

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

### Sprint 3 — Notifications, PDF Export & Realtime (Phụ trách: Phạm Đình Ánh Dương)
- [ ] **`TASK-311`** `[BE-Services - Phạm Đình Ánh Dương]` **Email Notification Service (SMTP)**
  - **Feature**: #33
  - **Target Files**: `backend/app/services/notification_service.py`
  - **Acceptance Criteria**: Sends email notifications when invited to event, when plan vote opens, and when plan is confirmed.
- [ ] **`TASK-312`** `[BE-Services - Phạm Đình Ánh Dương]` **PDF Export Service (WeasyPrint / ReportLab)**
  - **Feature**: #34
  - **Target Files**: `backend/app/api/v1/export.py`, `backend/app/services/export_service.py`
  - **Acceptance Criteria**: `GET /events/:id/export/pdf` generates downloadable PDF with event timeline, stop details, map snapshot, and expense summary.
- [ ] **`TASK-313`** `[BE-Services - Phạm Đình Ánh Dương]` **Packing Checklist Generation Service**
  - **Feature**: #35
  - **Target Files**: `backend/app/services/checklist_service.py`
  - **Acceptance Criteria**: Generates customizable packing list based on EventType and weather forecast.

### Sprint 4 — Admin Dashboard APIs & Realtime Server (Phụ trách: Phạm Đình Ánh Dương)
- [ ] **`TASK-405`** `[BE-Services - Phạm Đình Ánh Dương]` **Admin Statistics & Realtime APIs**
  - **Feature**: #36, #37
  - **Target Files**: `backend/app/api/v1/admin.py`, `backend/app/services/admin_service.py`
  - **Acceptance Criteria**: `GET /admin/dashboard/overview` returns total users, total events, token usage history, cache hit rate. `GET /admin/users` lists and manages user status.

---

## 🤝 Handover & Review Guidelines (Person 2)

1. **Buddy / Backup**: **Tạ Quang Huy** (Backend Dev A)
2. **Task Completion**: Run `pytest backend/tests/test_places.py` and `ruff check backend`. Push branch `feature/TASK-xxx` and tag `@BE-Core` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
