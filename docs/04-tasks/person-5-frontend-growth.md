# Person 5 — Frontend Dev B (AI Experience & Growth)

**Sở hữu**: UI Chat AI, Landing page, i18n, chia chi phí, Admin Dashboard UI.

## Sprint 0 — Contract
- [ ] Tham gia chốt OpenAPI spec `/ai/chat`, `/ai/orchestrator/run`, `/admin/*`
- [ ] Setup MSW mock cho `/ai/chat` (giả lập streaming response và đề xuất plan dạng card)

## Sprint 1 — Landing page + i18n khung
- [ ] Landing page giới thiệu *(#39)*, responsive, giới thiệu đầy đủ các loại sự kiện (du lịch, đi ăn, đi chơi, tham quan, cafe)
- [ ] Setup `react-i18next`, 2 ngôn ngữ VI/EN, key hoá toàn bộ text UI *(#40)*

## Sprint 2 — UI AI Chat (mock)
- [ ] Màn hình chat với AI *(#31, #32)* — dùng mock streaming response từ AI Engineer's state schema (đã có từ Sprint 0/1)
- [ ] UI hiển thị đề xuất Plan do AI tạo (dạng thẻ/card linh hoạt theo `StopCategory`: hiển thị menu cho quán ăn, giá vé cho chỗ chơi, hours/tips cho tham quan)

## Sprint 3 — Nối AI Chat thật + chia chi phí
- [ ] Tắt mock, nối `/ai/chat` thật (Integration Day với AI Engineer) — xử lý streaming SSE/WebSocket theo ADR đã chốt
- [ ] UI chia đều chi phí giữa thành viên event, chia theo hạng mục / món ăn *(#41)*

## Sprint 4 — Admin Dashboard UI
- [ ] UI hiển thị số liệu từ `/admin/dashboard/overview`, `/admin/usage/tokens` (Backend Dev B) *(#36, #37)*
- [ ] Biểu đồ token usage theo ngày/agent (dùng Recharts)
- [ ] Polish toàn bộ, test responsive, fix bug Integration Day *(#42)*

## Định nghĩa Done chung
- Chat UI xử lý đúng trạng thái: đang gõ, lỗi mạng, timeout — không đứng hình khi AI xử lý lâu
- i18n áp dụng cho toàn bộ text mới thêm, không hardcode string

## Không được tự ý làm khi chưa báo
- Đổi format message trong luồng chat (thêm field mới) → báo `#contract-changes`, AI Engineer đang code Chat Agent theo schema đã chốt.
