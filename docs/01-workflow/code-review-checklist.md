# Code Review Checklist

## Dành cho tác giả PR (tự kiểm tra trước khi request review)
- [ ] PR chỉ giải quyết **1 vấn đề/task**, diff lý tưởng < 400 dòng (nếu lớn hơn, cân nhắc tách nhỏ)
- [ ] Đã tự chạy lint + test local, CI xanh
- [ ] Đã cập nhật doc liên quan nếu đổi API/schema/kiến trúc (`03-architecture/`, `02-standards/api-design-guide.md`)
- [ ] Không còn `console.log`/code debug thừa, không có TODO không giải thích
- [ ] Không commit secrets/`.env`/API key (xem [security-guidelines.md](../05-security/security-guidelines.md))
- [ ] Đã điền đầy đủ template PR, mô tả rõ "làm gì" + "tại sao"
- [ ] Đã tự review lại diff của chính mình trên GitHub trước khi gắn reviewer

## Dành cho reviewer

### Đúng đắn (Correctness)
- [ ] Logic có đúng với yêu cầu task/Issue không?
- [ ] Có xử lý các edge case: input rỗng, null, số âm, mảng rỗng, timeout API bên thứ 3?
- [ ] Có race condition khi nhiều user cùng vote/sửa event không?

### Bảo mật
- [ ] Input từ user có được validate trước khi vào DB/AI Agent không? (chống SQL/Input injection & data corruption)
- [ ] Endpoint có đúng middleware Auth + kiểm tra phân quyền (Owner/Member/Viewer) không?
- [ ] Không có thông tin nhạy cảm bị log ra console/log file?

### Chất lượng code
- [ ] Đặt tên biến/hàm/class có tuân theo [naming-conventions.md](../02-standards/naming-conventions.md)?
- [ ] Có đoạn code trùng lặp nên tách hàm/service dùng chung không?
- [ ] Function có làm đúng 1 việc (Single Responsibility) không, có quá dài (>50 dòng) không?

### Test
- [ ] Có unit test cho logic mới/thay đổi không? (xem [testing-guide.md](../02-standards/testing-guide.md))
- [ ] Test có cover cả case fail, không chỉ happy path?

### Performance
- [ ] Có query N+1 vào DB không (đặc biệt ở Nhóm 2 — Event/Plan)?
- [ ] Có cache kết quả API bên thứ 3 khi phù hợp không (Nhóm 3)?
- [ ] Với AI Agent: có giới hạn số lần gọi LLM/loop vô hạn trong graph không?

### Kiến trúc & Docs
- [ ] Thay đổi có phá vỡ hợp đồng API với FE/Agent khác không? Đã thông báo team chưa?
- [ ] Docs liên quan đã được cập nhật trong cùng PR chưa?

## Mức độ comment khi review
| Prefix | Ý nghĩa |
|---|---|
| `[blocking]` | Bắt buộc sửa trước khi merge |
| `[suggestion]` | Gợi ý cải thiện, tác giả tự quyết định |
| `[question]` | Cần tác giả giải thích, không nhất thiết phải sửa |
| `[nit]` | Vấn đề rất nhỏ (style, chính tả), không chặn merge |

## Thời gian phản hồi
- Reviewer nên phản hồi PR trong vòng **24h** (ngày làm việc) để không chặn tiến độ nhóm khác đang phụ thuộc (đặc biệt PR liên quan schema DB — Nhóm 2).
