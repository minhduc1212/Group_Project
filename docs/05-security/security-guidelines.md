# Security Guidelines

## 1. Nguyên tắc chung
- **Không tự làm crypto/auth từ đầu** — dùng thư viện chuẩn đã kiểm chứng (PyJWT, bcrypt, passlib).
- **Validate mọi input ở boundary** (FastAPI Pydantic schemas), không tin dữ liệu từ client kể cả đã qua Frontend validate.
- **Least privilege**: mỗi request chỉ được làm đúng những gì role của user cho phép (xem ma trận quyền Owner/Member/Viewer ở `04-tasks/person-1-backend-core.md`).
- Áp dụng theo tinh thần **OWASP Top 10** cho web app thông thường + rủi ro riêng của hệ AI Agent (xem mục 4).

## 2. Quản lý secrets
- `.env` thật **không bao giờ** commit — đã có trong `.gitignore` ngay từ commit đầu tiên của repo.
- Chỉ commit `.env.example` với key rỗng/giá trị mẫu (xem file gốc `.env.example` ở root repo).
- Secrets môi trường CI/production lưu trong **GitHub Actions Secrets** / biến môi trường của platform hosting (Render/Railway/Vercel), không lưu trong code hay trong file config JSON commit lên repo.
- Nếu lỡ commit secret: **revoke/rotate key ngay lập tức** (không chỉ xoá khỏi commit sau — vì đã có trong lịch sử Git), sau đó dùng `git filter-repo`/BFG để xoá khỏi history nếu cần.

## 3. Auth & Session
- Password luôn hash bằng bcrypt (salt rounds ≥ 10), không bao giờ lưu plaintext dù chỉ tạm thời trong log.
- JWT access token thời gian sống ngắn (15 phút), refresh token dài hơn (7 ngày) lưu ở `httpOnly` + `Secure` cookie, không lưu ở `localStorage` (tránh XSS đánh cắp token).
- Endpoint reset password: token 1 lần dùng, hết hạn ngắn, không tiết lộ qua response khác biệt việc email có tồn tại hay không (chống enumeration).
- Rate limit endpoint auth (login, forgot-password) để chống brute-force.

## 4. Bảo mật riêng cho AI Multi-Agent System (phối hợp Nhóm 1 + Nhóm 4)

### 4.1 Chuẩn hóa Input & Message Roles
- Sử dụng cấu trúc message role (`system`/`user`/`assistant`) tách biệt của LLM API.
- Validate độ dài câu lệnh chat, giới hạn số lượt tool-calling liên tiếp trong 1 phiên (recursion_limit ≤ 15).
- Lọc bỏ mã độc hoặc ký tự bất thường (Sanitization qua Pydantic & bleach) trước khi truyền câu lệnh vào prompt.

### 4.2 Kiểm soát Output
- Output LLM luôn được validate qua Pydantic schema trước khi lưu DB hoặc thực hiện hành động (tạo Plan, gửi email...).
- AI không có quyền tự thực hiện hành động không thể đảo ngược mà không qua xác nhận người dùng (booking thật, thanh toán, xoá dữ liệu) — hiện tại Agent booking chỉ đưa **link**, không tự đặt hộ.
- Không hiển thị thẳng output LLM ra UI nếu output có thể chứa HTML/script chưa được escape (rủi ro XSS nếu render trực tiếp).

### 4.3 Giới hạn chi phí & lạm dụng
- Rate limit riêng cho `/api/v1/ai/*` theo user.
- Giới hạn số bước tối đa trong LangGraph state machine, timeout tổng cho 1 lần orchestrator chạy.
- Log đầy đủ vào `agent_logs` để phát hiện pattern bất thường (1 user gọi agent quá nhiều trong thời gian ngắn).

## 5. Bảo mật API chung
- CORS chỉ cho phép domain Frontend chính thức (`CORSMiddleware`), không để `*` ở production.
- Security headers middleware bật mặc định.
- SQL injection: dùng SQLAlchemy ORM (parameterized query mặc định) — không viết raw SQL nối chuỗi trực tiếp từ input user.
- File upload (nếu có, VD avatar) — giới hạn loại file, kích thước, scan/định dạng lại tên file, không dùng tên file gốc từ client để lưu trực tiếp.
- Dependency: chạy `pip audit` / Dependabot định kỳ, review PR tự động của Dependabot thay vì bỏ qua.

## 6. Checklist review bảo mật cho PR động vào Auth/AI (bắt buộc reviewer Security duyệt)
- [ ] Không có secret hardcode
- [ ] Input được validate đầy đủ (Pydantic schemas), không có field thừa được nhận vào
- [ ] Endpoint có đúng FastAPI Dependency phân quyền
- [ ] Không log dữ liệu nhạy cảm (password, token, API key) ra console/log file
- [ ] Rate limit đã áp dụng cho endpoint nhạy cảm/tốn chi phí

## 7. Báo cáo lỗ hổng nội bộ
- Phát hiện lỗ hổng trong quá trình dev → tạo Issue gắn label `security`, mức độ nghiêm trọng (`critical`/`high`/`medium`/`low`), tag `@security` + người phụ trách nhóm liên quan, xử lý ưu tiên trước feature mới nếu ở mức `critical`/`high`.
