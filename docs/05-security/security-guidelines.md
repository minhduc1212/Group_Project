# Security Guidelines

## 1. Nguyên tắc chung
- **Không tự làm crypto/auth từ đầu** — dùng thư viện chuẩn đã kiểm chứng (Passport, bcrypt, jsonwebtoken).
- **Validate mọi input ở boundary** (controller/DTO), không tin dữ liệu từ client kể cả đã qua Frontend validate.
- **Least privilege**: mỗi request chỉ được làm đúng những gì role của user cho phép (xem ma trận quyền Owner/Member/Viewer ở `04-tasks/person-1-backend-core.md`).
- Áp dụng theo tinh thần **OWASP Top 10** cho web app thông thường + rủi ro riêng của hệ AI Agent (xem mục 4).

## 2. Quản lý secrets
- `.env` thật **không bao giờ** commit — đã có trong `.gitignore` ngay từ commit đầu tiên của repo.
- Chỉ commit `.env.example` với key rỗng/giá trị mẫu (xem file gốc `docs/.env.example`).
- Secrets môi trường CI/production lưu trong **GitHub Actions Secrets** / biến môi trường của platform hosting (Render/Railway/Vercel), không lưu trong code hay trong file config JSON commit lên repo.
- Nếu lỡ commit secret: **revoke/rotate key ngay lập tức** (không chỉ xoá khỏi commit sau — vì đã có trong lịch sử Git), sau đó dùng `git filter-repo`/BFG để xoá khỏi history nếu cần.

## 3. Auth & Session
- Password luôn hash bằng bcrypt (salt rounds ≥ 10), không bao giờ lưu plaintext dù chỉ tạm thời trong log.
- JWT access token thời gian sống ngắn (15 phút), refresh token dài hơn (7 ngày) lưu ở `httpOnly` + `Secure` cookie, không lưu ở `localStorage` (tránh XSS đánh cắp token).
- Endpoint reset password: token 1 lần dùng, hết hạn ngắn, không tiết lộ qua response khác biệt việc email có tồn tại hay không (chống enumeration).
- Rate limit endpoint auth (login, forgot-password) để chống brute-force.

## 4. Bảo mật riêng cho AI Multi-Agent System (phối hợp Nhóm 1 + Nhóm 4)

### 4.1 Chống Prompt Injection
- Không nối chuỗi thô input người dùng trực tiếp vào system prompt — dùng cấu trúc message role (`system`/`user`) tách biệt của LLM API.
- Với nội dung lấy từ nguồn ngoài (review địa điểm, dữ liệu Agent research lấy từ web) — coi là **dữ liệu chưa tin cậy**, không cho phép nó override instruction hệ thống; đánh dấu rõ ràng trong prompt đây là "dữ liệu tham khảo", không phải chỉ thị.
- Giới hạn độ dài input chat, giới hạn số lượt tool-calling liên tiếp trong 1 phiên.

### 4.2 Kiểm soát Output
- Output LLM luôn được validate qua schema (Zod) trước khi lưu DB hoặc thực hiện hành động (tạo Plan, gửi email...).
- AI không có quyền tự thực hiện hành động không thể đảo ngược mà không qua xác nhận người dùng (booking thật, thanh toán, xoá dữ liệu) — hiện tại Agent booking chỉ đưa **link**, không tự đặt hộ.
- Không hiển thị thẳng output LLM ra UI nếu output có thể chứa HTML/script chưa được escape (rủi ro XSS nếu render trực tiếp).

### 4.3 Giới hạn chi phí & lạm dụng
- Rate limit riêng cho `/ai/*` theo user.
- Giới hạn số bước tối đa trong LangGraph state machine, timeout tổng cho 1 lần orchestrator chạy.
- Log đầy đủ vào `agent_logs` để phát hiện pattern bất thường (1 user gọi agent quá nhiều trong thời gian ngắn).

## 5. Bảo mật API chung
- CORS chỉ cho phép domain Frontend chính thức, không để `*` ở production.
- Helmet middleware (security headers) bật mặc định ở NestJS.
- SQL injection: dùng Prisma (parameterized query mặc định) — không viết raw SQL nối chuỗi trực tiếp từ input user.
- File upload (nếu có, VD avatar) — giới hạn loại file, kích thước, scan/định dạng lại tên file, không dùng tên file gốc từ client để lưu trực tiếp.
- Dependency: chạy `npm audit` / Dependabot định kỳ, review PR tự động của Dependabot thay vì bỏ qua.

## 6. Checklist review bảo mật cho PR động vào Auth/AI (bắt buộc reviewer Security duyệt)
- [ ] Không có secret hardcode
- [ ] Input được validate đầy đủ (DTO/Zod), không có field thừa được nhận vào (`whitelist`)
- [ ] Endpoint có đúng Guard phân quyền
- [ ] Nếu liên quan AI: đã kiểm tra chống prompt injection theo mục 4.1
- [ ] Không log dữ liệu nhạy cảm (password, token, API key) ra console/log file
- [ ] Rate limit đã áp dụng cho endpoint nhạy cảm/tốn chi phí

## 7. Báo cáo lỗ hổng nội bộ
- Phát hiện lỗ hổng trong quá trình dev → tạo Issue gắn label `security`, mức độ nghiêm trọng (`critical`/`high`/`medium`/`low`), tag `@security` + người phụ trách nhóm liên quan, xử lý ưu tiên trước feature mới nếu ở mức `critical`/`high`.
