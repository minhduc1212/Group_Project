# Contract-First Workflow — Cơ chế để 6 người làm song song

## 1. Vấn đề cần giải quyết
Nếu code tuần tự "Backend xong API → Frontend mới code UI → AI Engineer mới code Agent", 6 người sẽ **không chạy song song được**, biến 6 người thành làm việc như 2–3 người (người sau luôn chờ người trước). Cách công ty chuyên nghiệp giải quyết: **chốt hợp đồng giao diện (contract) trước khi viết code triển khai**, rồi ai cũng code song song dựa trên contract đó.

## 2. "Contract" gồm những gì?
1. **Database schema** (Prisma) — xem [database-schema.md](docs/03-architecture/database-schema.md)
2. **OpenAPI/Swagger spec** — toàn bộ endpoint, request/response shape — xem [api-design-guide.md](docs/02-standards/api-design-guide.md)
3. **Shared types/DTO** (Zod schema hoặc TypeScript type) đặt trong `packages/shared-types/` — dùng chung cho Backend, Frontend, AI Service để không lệch kiểu dữ liệu

## 3. Quy trình "Sprint 0 — Contract Session" (bắt buộc, làm trước khi tách nhau code)
**Thời lượng: 1–2 ngày đầu dự án, cả 6 người tham gia cùng lúc.**

1. Backend Dev A trình bày schema DB đề xuất (dựa trên `database-schema.md` khởi điểm trong docs này) → cả team góp ý trực tiếp, đặc biệt AI Engineer (cần field gì cho Agent) và Frontend (cần field gì để hiển thị).
2. Thống nhất toàn bộ endpoint trong `api-design-guide.md` — thêm/bớt nếu cần, chốt request/response shape.
3. Backend Dev A tạo file `openapi.yaml` (hoặc dùng `@nestjs/swagger` sinh ra từ DTO rỗng — controller chỉ có signature, chưa có logic thật) + chạy migration DB thật.
4. Push contract lên nhánh `main`/`develop` — đây là **mốc khởi động** để 5 người còn lại bắt đầu code song song.

## 4. Sau Contract Session — ai làm gì song song

### Backend Dev A & B
- Code logic thật cho service/controller theo đúng signature đã chốt.

### AI Engineer
- Không chờ Backend code xong logic thật. Dùng ngay:
  - Schema Prisma đã có (đọc field, không cần data thật) để định nghĩa Zod schema output của Agent.
  - Mock data (`fixtures/mock-events.json`) tự tạo theo đúng schema đã chốt, để test Agent logic.
  - Gọi thẳng Backend Dev A's endpoint đã deploy ở môi trường dev ngay khi có (kể cả trả `501 Not Implemented` tạm — miễn đúng response shape) để test tích hợp sớm.

### Frontend Dev A & B
- Dùng **MSW (Mock Service Worker)** trong `frontend/src/mocks/`: định nghĩa response giả lập đúng theo OpenAPI contract đã chốt.
- Code UI, gọi API qua đúng URL/shape thật — chỉ khác là response đến từ MSW thay vì server thật.
- Khi Backend deploy xong thật ở `staging` → tắt MSW, trỏ thẳng API thật, không phải sửa code gọi API (vì đã đúng contract từ đầu).

### Security & DevOps
- Không chờ có code để "review". Dựng ngay từ Sprint 0:
  - CI/CD pipeline (lint, test, build) — chạy trên khung project rỗng cũng được.
  - Docker Compose cho local dev (Postgres, Redis) — ai cũng cần cái này ngay ngày 1.
  - Threat model sơ bộ cho hệ AI Agent (dựa trên kiến trúc đã chốt) — viết checklist review trước khi có PR đầu tiên.

## 5. Quy tắc thay đổi contract giữa chừng
- Đổi contract (thêm field, đổi response shape) **không được tự ý đổi âm thầm** — vì 4-5 người khác đang code dựa trên contract cũ.
- Quy trình đổi:
  1. Mở Issue/thông báo kênh `#contract-changes`, nêu rõ đổi gì, ảnh hưởng ai.
  2. Cập nhật `api-design-guide.md`/`database-schema.md`/`shared-types` trong 1 PR riêng, review nhanh (ưu tiên, không để tồn đọng).
  3. Người bị ảnh hưởng cập nhật mock/code của mình theo contract mới.
- Hạn chế đổi contract sau Sprint 1 — nếu bắt buộc đổi, ưu tiên **thêm field mới** (backward-compatible) thay vì đổi/xoá field cũ.

## 6. Integration Day
- Cuối mỗi sprint, dành **nửa ngày** để nối thật: Frontend tắt mock trỏ Backend thật, AI Engineer chạy full flow với DB thật, Security chạy quét bảo mật trên bản build thật.
- Bug phát hiện ở Integration Day ưu tiên xử lý trước khi nhận task mới của sprint tiếp theo.
