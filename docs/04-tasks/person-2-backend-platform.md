# Person 2 — Backend Dev B (Platform & Integration)

**Sở hữu**: External API/Cache (N3) + Notification/Export (N5) + Admin (N6).
**Đặc điểm**: Mảng này ít phụ thuộc Backend Dev A nhất ở giai đoạn đầu → có thể chạy độc lập ngay từ Sprint 1.

## Sprint 0 — Contract
- [ ] Chốt OpenAPI spec `/places/*`, `/hotels/*`, `/weather`, `/exchange-rate`, `/notifications/*`, `/export/*`, `/admin/*` cùng team (sinh tự động qua FastAPI `/docs`)
- [ ] Setup Redis cache layer khung sườn (`redis-py` async, dùng chung với Backend Dev A)

## Sprint 1 — External API + cache (HTTPX async + redis-py)
- [ ] Tra cứu địa điểm (Google Places API qua `httpx.AsyncClient`) hỗ trợ category filter: `RESTAURANT`, `CAFE`, `ENTERTAINMENT`, `ATTRACTION`, `HOTEL` *(#17)*
- [ ] So sánh dữ liệu khách sạn *(#18)*
- [ ] Currency Converter *(#21)*
- [ ] Cache Redis cho từng loại API (TTL khác nhau theo `system-architecture.md`)
- **Đồng bộ**: Chuẩn hoá Pydantic response schema (kèm metadata cho từng category) cùng AI Engineer trước khi họ code Location/Research Agent (họ dùng data này làm input).

## Sprint 2 — Hoàn thiện tích hợp
- [ ] API thời tiết (OpenWeatherMap via `httpx`) *(nền cho #20, #28, #35)*
- [ ] Cấp public token Mapbox an toàn cho Frontend *(#19)*
- [ ] Đo cache hit/miss ratio cơ bản, log ra để Admin Dashboard dùng sau *(#22)*

## Sprint 3 — Notification & Export
- [ ] Cron job / APScheduler nhắc lịch trình / vote sắp đóng / lời mời nợ trả lời *(#33)*
- [ ] Export PDF lịch trình (WeasyPrint / ReportLab) — render timeline + bản đồ + chi phí *(#34)*
- [ ] Checklist chuẩn bị đồ theo loại event & thời tiết *(#35)*

## Sprint 4 — Admin Dashboard (BE FastAPI)
- [ ] `GET /api/v1/admin/users`, `GET /api/v1/admin/usage/tokens`, `GET /api/v1/admin/dashboard/overview` *(#36, #37)*
- [ ] `AdminGuard` dependency riêng
- [ ] Tổng hợp dữ liệu từ bảng `agent_logs` (AI Engineer ghi log) + `events`/`users` (Backend Dev A)

## Định nghĩa Done chung
- Mọi external call qua `httpx` có timeout + retry giới hạn + fallback rõ ràng
- Pytest mock external API (không gọi thật trong CI)

## Không được tự ý làm khi chưa báo
- Đổi format Pydantic schema của `/places/*`, `/weather` → AI Engineer đang build Agent dựa trên format này, báo trước ở `#contract-changes`.
