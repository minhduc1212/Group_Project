# Project Overview

## 1. Tên dự án
Web lên kế hoạch nhóm tích hợp AI Multi-Agent — nền tảng lên kế hoạch hoạt động nhóm (du lịch, ăn uống, vui chơi, tham quan, cafe...), có hệ thống AI Agent hỗ trợ tìm địa điểm, tạo lịch trình, quản lý ngân sách và phân giải xung đột ý kiến giữa các thành viên.

## 2. Bài toán & Mục tiêu
- Nhóm bạn/gia đình thường tốn nhiều thời gian bàn bạc khi lên kế hoạch cùng nhau — không chỉ du lịch mà cả chọn quán ăn, chỗ chơi, điểm tham quan, cafe gặp mặt.
- Dự án xây dựng một hệ thống **Event → Plan → Vote** làm xương sống hỗ trợ nhiều loại sự kiện (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM), và gắn một **hệ Multi-Agent AI** (orchestrator + sub-agents) vào để tự động hoá phần nghiên cứu, đề xuất, tính chi phí, giải quyết xung đột vote.
- Trọng tâm chấm điểm/đánh giá kỹ thuật: **Nhóm 4 (AI Multi-Agent System)**.

## 3. Phạm vi (Scope)
### Trong phạm vi (MVP)
- Auth (Google/Facebook OAuth2, JWT)
- CRUD Event/Plan/Vote, phân quyền Owner/Member/Viewer
- Hỗ trợ nhiều loại sự kiện: du lịch, ăn uống, vui chơi giải trí, tham quan, cafe/hangout, tùy chỉnh
- Plan thủ công (không dùng AI) cũng có đầy đủ luồng Vote → Confirm → Export
- Tra cứu địa điểm/khách sạn/thời tiết/tỷ giá qua API bên thứ 3
- Multi-Agent: orchestrator, booking, tìm địa điểm, tạo plan, research, phân giải xung đột, chat, tính chi phí
- Notification email, export PDF, checklist
- Landing page, i18n, chia đều chi phí

### Ngoài phạm vi MVP (tính sau — "backlog")
- Premium/giới hạn lượt dùng (#10)
- Tham khảo plan người khác công khai (#13)
- Admin Dashboard nâng cao (billing, revenue chi tiết)

## 4. Đối tượng người dùng
- Nhóm bạn/gia đình (2–10 người), cần đồng thuận nhanh khi lên kế hoạch cùng nhau — đi du lịch, đi ăn, đi chơi, tham quan, gặp mặt.

## 5. Chỉ số thành công (định hướng)
- Thời gian trung bình để 1 nhóm chốt được lịch trình (từ tạo event → chốt plan).
- Tỷ lệ đề xuất của AI Agent được người dùng chấp nhận không cần chỉnh sửa.
- Độ chính xác của Agent phân giải xung đột vote (so với quyết định thủ công).

## 6. Ràng buộc kỹ thuật
- Ngân sách API bên thứ 3 giới hạn (sinh viên/đồ án) → bắt buộc có **caching** cho Nhóm 3.
- Chi phí LLM API → cần theo dõi token usage (Nhóm 6 — Admin Dashboard).
- Thời gian đồ án có hạn → xem lộ trình phụ thuộc ở [task-board.md](../04-tasks/task-board.md).
