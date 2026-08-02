# Documentation Guide

## 1. Nguyên tắc "Docs as Code"
- Toàn bộ tài liệu sống trong repo dưới dạng Markdown (`/docs`), **được review qua PR** giống code.
- Không dùng Google Docs/Notion rời rạc cho tài liệu kỹ thuật lâu dài (chỉ dùng cho brainstorm tạm thời) — vì dễ lệch với code thực tế theo thời gian.
- Thay đổi ảnh hưởng kiến trúc/API/schema **bắt buộc** cập nhật doc tương ứng trong cùng PR với code.

## 2. README cấp module/service
Mỗi service (`backend/`, `frontend/`, `ai-service/` nếu tách riêng) có 1 `README.md` gốc gồm tối thiểu:
```markdown
# <Tên service>

## Mô tả ngắn
## Yêu cầu hệ thống (Node version, ...)
## Cài đặt
​```bash
npm install
cp .env.example .env
npm run dev
​```
## Scripts chính
| Lệnh | Mô tả |
|---|---|
| npm run dev | ... |
| npm run test | ... |
| npm run lint | ... |

## Cấu trúc thư mục
## Liên kết docs liên quan
```

## 3. Comment trong code
### Backend/Frontend (TypeScript) — dùng JSDoc cho hàm/service public
```ts
/**
 * Tạo event mới và tự động thêm người tạo làm Owner.
 * @param dto - Dữ liệu tạo event đã được validate
 * @param userId - ID người dùng đang thực hiện (lấy từ JWT)
 * @returns Event vừa tạo kèm thông tin member
 * @throws BadRequestException nếu ngày kết thúc trước ngày bắt đầu
 */
async createEvent(dto: CreateEventDto, userId: string): Promise<Event> { ... }
```
- **Không comment những gì code đã tự nói rõ** (VD `// tăng i lên 1` cho `i++` là thừa).
- Comment giải thích **"tại sao"** khi logic không hiển nhiên (VD: vì sao dùng transaction, vì sao retry 3 lần).

### AI Agent / Prompt
- Mỗi prompt template có comment mô tả: mục đích, input mong đợi, output schema, model đang dùng, ngày cập nhật lần cuối.

## 4. Architecture Decision Record (ADR)
Khi có quyết định kỹ thuật quan trọng (đổi DB, đổi thư viện orchestration, đổi cấu trúc Auth...), ghi lại theo template ngắn trong `03-architecture/adr/`:
```markdown
# ADR-001: Chọn LangGraph.js thay vì tự viết orchestrator

## Bối cảnh
## Các phương án đã xét
## Quyết định
## Hệ quả (đánh đổi gì)
## Ngày & người quyết định
```
Giúp người sau (hoặc chính mình 2 tuần sau) hiểu **vì sao** hệ thống được làm như vậy, không chỉ **cái gì**.

## 5. Quy tắc viết Markdown
- Tiêu đề dùng `#`/`##`/`###` đúng phân cấp, không nhảy cấp (H1 → H3).
- Code block luôn khai báo ngôn ngữ (` ```ts `, ` ```bash `) để syntax highlight đúng.
- Bảng dùng cho dữ liệu so sánh/liệt kê có cấu trúc thay vì đoạn văn dài.
- Link chéo giữa các file docs dùng **relative path** (`../02-standards/...`), không dùng absolute URL nội bộ, để còn hoạt động khi đổi domain repo.
- Tên file: `kebab-case.md`, tiếng Anh (để đồng bộ với code), nội dung có thể viết tiếng Việt.

## 6. Ngôn ngữ
- Docs kỹ thuật (naming, workflow) có thể viết tiếng Việt cho dễ hiểu trong team.
- Comment trong code, tên biến/hàm, commit message: **tiếng Anh** (chuẩn ngành, dễ nếu sau này public repo/portfolio).
