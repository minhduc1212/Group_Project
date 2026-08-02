# Danh Sách Tính Năng
## Dự án: Web Lên Kế Hoạch Nhóm Tích Hợp AI Multi-Agent

---

## Các loại sự kiện hỗ trợ (EventType)

| Loại | Ví dụ |
|---|---|
| `TRAVEL` | Đà Lạt 3N2Đ, Phú Quốc 5 ngày |
| `DINING` | "Tối nay ăn gì?" — chọn quán, chọn món |
| `HANGOUT` | Cafe chiều thứ 7, gặp mặt bạn bè |
| `ENTERTAINMENT` | Karaoke, bowling, escape room, arcade |
| `SIGHTSEEING` | Bảo tàng, triển lãm, di tích, check-in |
| `CUSTOM` | Teambuilding, sinh nhật, picnic |

---

## Nhóm 1 — Tài Khoản & Bảo Mật

| # | Tính năng | Mô tả |
|---|---|---|
| 1 | Đăng nhập OAuth | Login qua Google / Facebook |
| 2 | Đăng ký tài khoản | Email + mật khẩu (hash bcrypt) |
| 3 | Quên mật khẩu | Gửi email reset password, token 1 lần |
| 4 | Hồ sơ cá nhân | Tạo / xem / sửa profile (tên, avatar) |
| 5 | Refresh Token | Tự động gia hạn phiên đăng nhập |

---

## Nhóm 2 — Quản Lý Event & Plan

| # | Tính năng | Mô tả |
|---|---|---|
| 6 | Tạo event | Chọn loại (TRAVEL / DINING / ENTERTAINMENT / ...), đặt tên, ngày, khu vực |
| 7 | Mời thành viên | Gửi lời mời qua link / email, quản lý trạng thái (Pending / Accepted / Declined) |
| 8 | Phân quyền | Owner / Member / Viewer — mỗi role có hành động khác nhau |
| 9 | Xem & quản lý event | Danh sách event, lịch sử, tìm kiếm |
| 10 | Xem các plan trong event | Danh sách plan (AI + thủ công), so sánh |
| 11 | Tạo plan thủ công | Tự thêm điểm dừng bằng tay, có autocomplete Google Places. **Đi qua luồng Vote → Confirm giống plan AI** |
| 12 | Chỉnh sửa plan | Đổi thứ tự điểm dừng, xóa / thêm stop, sửa ghi chú |
| 13 | Vote cho plan | Mỗi member vote UP / DOWN / NEUTRAL + comment góp ý |
| 14 | Xác nhận plan | Chỉ Owner mới confirm plan → chuyển DRAFT → CONFIRMED |
| 15 | Lưu yêu thích | Lưu danh sách địa điểm / quán ăn / chỗ chơi yêu thích |
| 16 | Tham khảo plan công khai | Xem plan của nhóm khác để lấy ý tưởng *(backlog)* |

---

## Nhóm 3 — Tra Cứu & Tích Hợp Bên Ngoài

| # | Tính năng | Mô tả |
|---|---|---|
| 17 | Tra cứu địa điểm | Tìm điểm du lịch, nhà hàng, quán cafe, chỗ chơi, điểm tham quan (Google Places) |
| 18 | So sánh khách sạn | So sánh giá, đánh giá, tiện nghi giữa các khách sạn |
| 19 | Hiển thị bản đồ | Bản đồ tương tác hiển thị các stop trong plan (Mapbox / Google Maps) |
| 20 | Thời tiết | Tra cứu thời tiết điểm đến (OpenWeatherMap) |
| 21 | Chuyển đổi tiền tệ | Quy đổi tỷ giá giữa các đồng tiền |
| 22 | Cache dữ liệu | Cache kết quả API bên thứ 3 qua Redis (tránh vượt rate limit) |

---

## Nhóm 4 — Hệ Thống AI Multi-Agent ⭐ (trọng tâm đồ án)

| # | Tính năng | Mô tả |
|---|---|---|
| 23 | Orchestrator Agent | Điều phối toàn bộ sub-agent, routing theo EventType |
| 24 | Location Agent | Tìm địa điểm / nhà hàng / quán cafe / chỗ chơi phù hợp yêu cầu nhóm |
| 25 | Research Agent | Tổng hợp review, thông tin chi tiết, gợi ý menu/món ăn (DINING), giá vé (ENTERTAINMENT) |
| 26 | Plan Agent | Tạo lịch trình tối ưu theo ngày, quản lý ngân sách |
| 27 | Booking Agent | Đưa link đặt khách sạn / đặt bàn / đặt vé (không tự đặt hộ) |
| 28 | Note Agent | Gợi ý lưu ý khi đi (thời tiết, đồ mang theo, tips) |
| 29 | Cost Agent | Tính tổng chi phí, chia đều / chia theo món cho nhóm |
| 30 | Conflict Resolver Agent | Phân giải xung đột khi vote hòa, đề xuất phương án dung hòa |
| 31 | Chat Agent | Hội thoại tự do với AI, hỗ trợ streaming (SSE / WebSocket) |
| 32 | Màn hình chat | UI chat với AI, hiển thị đề xuất plan dạng card/timeline |

---

## Nhóm 5 — Thông Báo & Xuất Dữ Liệu

| # | Tính năng | Mô tả |
|---|---|---|
| 33 | Nhắc nhở email | Nhắc lịch trình sắp đến, vote sắp đóng, lời mời chưa trả lời |
| 34 | Export PDF | Xuất lịch trình ra file PDF (bản đồ + timeline + chi phí) |
| 35 | Checklist chuẩn bị | Danh sách đồ cần mang theo, tùy theo loại event và thời tiết |

---

## Nhóm 6 — Quản Trị Hệ Thống

| # | Tính năng | Mô tả |
|---|---|---|
| 36 | Admin Dashboard | Thống kê user, event, token/chi phí API, cache hit rate |
| 37 | Quản lý người dùng | Xem / khóa / xóa tài khoản |
| 38 | Giới hạn lượt dùng AI | Rate limit theo user, cảnh báo khi gần hết quota *(backlog)* |

---

## Nhóm 7 — Giao Diện & Trải Nghiệm Chung

| # | Tính năng | Mô tả |
|---|---|---|
| 39 | Landing page | Giới thiệu trang web, tính năng, CTA đăng ký |
| 40 | Đa ngôn ngữ (i18n) | Hỗ trợ Tiếng Việt / English |
| 41 | Chia sẻ chi phí | Chia đều hoặc chia theo mục cho thành viên event |
| 42 | Responsive UI | Tương thích mobile, tablet, desktop |
