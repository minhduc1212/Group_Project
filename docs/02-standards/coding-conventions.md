# Coding Conventions

Áp dụng chung: **TypeScript strict mode bật ở cả FE & BE**, ESLint + Prettier bắt buộc, format tự động qua pre-commit hook (Husky + lint-staged).

## 1. Cấu hình chung bắt buộc
```jsonc
// tsconfig.json (rút gọn)
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  }
}
```
- ESLint: `eslint:recommended` + `@typescript-eslint/recommended` + plugin riêng theo framework (`eslint-plugin-react-hooks` cho FE).
- Prettier: 2 spaces, single quotes, dấu `;` cuối dòng, `printWidth: 100`.
- Chạy `lint` + `format:check` trong CI, PR fail nếu vi phạm.

## 2. Backend (NestJS)
- Cấu trúc module theo **Domain**, không theo Layer phẳng:
  ```
  src/
    modules/
      auth/
        auth.controller.ts
        auth.service.ts
        auth.module.ts
        dto/
        guards/
      event/
      plan/
      vote/
      ai-agent/
        orchestrator/
        agents/
          booking.agent.ts
          location.agent.ts
          plan.agent.ts
          ...
    common/          # filter, pipe, interceptor, decorator dùng chung
    config/
  ```
- **Controller**: chỉ nhận request, validate DTO, gọi Service — không chứa business logic.
- **Service**: chứa business logic, không biết gì về HTTP (dễ test, dễ tái sử dụng cho Agent gọi trực tiếp).
- **DTO** dùng `class-validator` decorator, không nhận field thừa (`whitelist: true` ở ValidationPipe toàn cục).
- Mọi endpoint ghi dữ liệu (`POST/PUT/PATCH/DELETE`) phải qua Guard kiểm tra quyền (Owner/Member/Viewer).
- Không throw lỗi generic `Error` — dùng NestJS Exception (`BadRequestException`, `ForbiddenException`,...) để trả HTTP status đúng.

## 3. Frontend (React + TypeScript)
- Cấu trúc theo **feature folder**:
  ```
  src/
    features/
      auth/
      event/
      plan/
      ai-chat/
    components/ui/     # component dùng chung (button, input,...)
    hooks/
    lib/                 # axios instance, query client, utils
    stores/               # zustand stores
  ```
- Component function, không dùng class component.
- 1 file = 1 component chính, đặt tên file trùng tên component (`EventCard.tsx` chứa `EventCard`).
- Tách logic gọi API ra custom hook (`useCreateEvent.ts`) dùng TanStack Query, không gọi `fetch`/`axios` trực tiếp trong component.
- Không để logic nghiệp vụ phức tạp trong JSX — tách hàm helper hoặc hook riêng.

## 4. AI Agent (LangGraph)
- Mỗi Agent là 1 file/module riêng trong `modules/ai-agent/agents/`, có input/output schema rõ ràng (dùng Zod để validate output LLM trả về — không tin tưởng 100% JSON từ LLM).
- Prompt template tách riêng khỏi logic code (file `.prompt.ts` hoặc thư mục `prompts/`), có version comment ở đầu file khi thay đổi đáng kể.
- Orchestrator không gọi thẳng LLM cho logic có thể làm bằng code thường (VD: tính tổng chi phí nên là hàm thuần, không cần LLM).
- Luôn có giới hạn số vòng lặp/số lần gọi tool trong graph (tránh loop vô hạn tốn chi phí API).
- Log lại: input, output, số token, thời gian xử lý của mỗi lần gọi Agent (phục vụ Admin Dashboard Nhóm 6 + debug).

## 5. Quy tắc chung mọi ngôn ngữ
- Không magic number/string — khai báo hằng số có tên rõ nghĩa.
- Hàm nên < 50 dòng; nếu dài hơn, cân nhắc tách nhỏ.
- Xử lý lỗi rõ ràng (try/catch có ý nghĩa), không nuốt lỗi im lặng (`catch (e) {}` rỗng là **cấm**).
- Không comment code chết (code cũ để đó "phòng khi cần") — dùng Git history thay vì comment-out.
