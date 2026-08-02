# Person 4 — Frontend Dev A (Core Flows UI)

**Sở hữu**: UI cho Auth, Event, Plan, Vote, Checklist. Code song song với Backend Dev A qua mock (MSW), nối thật ở Integration Day.

## Sprint 0 — Contract
- [ ] Tham gia chốt OpenAPI spec — góp ý shape response cần cho UI (VD cần field nào để hiển thị list, metadata cho từng category)
- [ ] Setup MSW (`frontend/src/mocks/`), viết handler mock cho `/auth/*`, `/events/*`, `/invitations/*`, `/plans/*`, `/votes/*` đúng theo contract

## Sprint 1 — UI Auth (mock API)
- [ ] Màn hình Login (Google/Facebook button), Register, Forgot Password *(#1, #2, #3)*
- [ ] Màn hình Profile (xem/sửa) *(#4)*
- [ ] Xử lý lưu token đúng chuẩn bảo mật (không lưu access token nhạy cảm ở `localStorage`, dùng cookie httpOnly do BE set) *(#5)*
- **Mốc cuối sprint**: Integration Day — tắt mock `/auth/*`, nối API thật của Backend Dev A.

## Sprint 2 — UI Event/Plan/Vote (mock API)
- [ ] Màn hình tạo Event (chọn EventType: TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM), xem/sửa Event *(#6, #9)*
- [ ] UI Mời thành viên & Quản lý lời mời (gửi link/email, danh sách lời mời Pending/Accepted/Declined) *(#7)*
- [ ] Màn hình danh sách Plan trong Event (phân biệt Plan AI vs Plan Thủ công) *(#10)*
- [ ] UI hiển thị theo Role (Owner / Member / Viewer thấy nút hành động khác nhau) *(#8)*
- [ ] Tích hợp bản đồ hiển thị (dùng token public từ Backend Dev B) *(#19)*

## Sprint 3 — Nối API thật + Manual Plan + Vote UI
- [ ] Tắt toàn bộ mock Event/Plan/Vote, nối API thật (Integration Day)
- [ ] UI Tạo & Chỉnh sửa Plan thủ công (thêm stop với Google Places autocomplete, sửa thứ tự drag & drop) *(#11, #12)*
- [ ] UI Vote + hiển thị kết quả tổng hợp + chuyển trạng thái Plan (Gửi vote → Confirm) *(#13, #14)*
- [ ] UI Checklist chuẩn bị đồ *(#35)*

## Sprint 4 — Polish & test
- [ ] Component test (Vitest + RTL) cho các flow chính: login, tạo event, vote, manual plan
- [ ] Responsive mobile, xử lý loading/error state đầy đủ (TanStack Query)
- [ ] Fix bug từ Integration Day + Pentest (Security)

## Định nghĩa Done chung
- Không gọi `fetch`/`axios` trực tiếp trong component — qua custom hook TanStack Query
- Test coverage các flow chính có RTL test

## Không được tự ý làm khi chưa báo
- Nếu phát hiện contract API thiếu field cần cho UI → báo `#contract-changes`, không tự chế field phía FE rồi Backend phải chạy theo sau.
