# Coding Conventions

Áp dụng chung: **Python 3.11+ PEP 8 (Ruff/Black) cho Backend & AI Agent**, **TypeScript strict mode cho Frontend**, linter/formatter tự động qua pre-commit hook (Husky / pre-commit).

## 1. Cấu hình chung bắt buộc
- **Backend (Python)**:
  - PEP 8 standard, type hints bắt buộc cho mọi function parameters và return types.
  - Formatter: `black` hoặc `ruff format` (line-length: 100).
  - Linter: `ruff` (bắt lỗi import, unused variables, type safety).
  - Type checker: `mypy` (strict mode).
- **Frontend (TypeScript)**:
  - ESLint: `eslint:recommended` + `@typescript-eslint/recommended` + `eslint-plugin-react-hooks`.
  - Prettier: 2 spaces, single quotes, dấu `;` cuối dòng, `printWidth: 100`.
- Chạy `ruff check .` và `npm run lint` trong CI, PR fail nếu vi phạm style code.

## 2. Backend (Python FastAPI)
- Cấu trúc module theo **Domain-Driven Layout**:
  ```
  app/
    core/             # Security, DB engine, config BaseSettings
    models/           # SQLAlchemy DB models (User, Event, Plan, Vote...)
    schemas/          # Pydantic v2 Request/Response DTOs
    api/
      v1/
        auth.py       # FastAPI APIRouter for /auth
        events.py     # FastAPI APIRouter for /events
        plans.py      # FastAPI APIRouter for /plans
        votes.py      # FastAPI APIRouter for /votes
        places.py     # FastAPI APIRouter for /places
        ai.py         # FastAPI APIRouter for /ai
    services/         # Business logic & DB queries
    ai_agents/        # LangGraph Multi-Agent system
      orchestrator.py
      agents/
        booking.py
        location.py
        plan.py
        ...
  ```
- **APIRouter (Controller)**: chỉ nhận HTTP request, dependency injection (`Depends`), validate Pydantic schema, gọi Service — không chứa business logic phức tạp.
- **Service Layer**: hàm `async def`, làm việc với SQLAlchemy `AsyncSession`, không dính dáng đến HTTP status code (dễ test bằng Pytest).
- **Pydantic Schemas**: dùng Pydantic v2 `BaseModel`, thiết lập `extra = "forbid"` để chặn field thừa.
- Mọi endpoint ghi dữ liệu (`POST/PUT/PATCH/DELETE`) phải qua `get_current_user` dependency để kiểm tra JWT token và phân quyền Owner/Member/Viewer.
- Không throw lỗi generic `Exception` — dùng `HTTPException(status_code=..., detail=...)` hoặc custom exception handlers với code UPPER_SNAKE_CASE.

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
    lib/               # axios instance, query client, utils
    stores/            # zustand stores
  ```
- Component function, không dùng class component.
- 1 file = 1 component chính, đặt tên file trùng tên component (`EventCard.tsx` chứa `EventCard`).
- Tách logic gọi API ra custom hook (`useCreateEvent.ts`) dùng TanStack Query, không gọi `fetch`/`axios` trực tiếp trong component.
- Không để logic nghiệp vụ phức tạp trong JSX — tách hàm helper hoặc hook riêng.

## 4. AI Agent (LangGraph Python)
- Mỗi Agent là 1 module riêng trong `app/ai_agents/agents/`, có input/output state rõ ràng (dùng Pydantic `BaseModel` để validate output LLM trả về).
- Prompt template tách riêng khỏi logic code (file `prompts.py` hoặc thư mục `prompts/`), có version comment ở đầu file khi thay đổi đáng kể.
- Orchestrator không gọi LLM cho logic có thể làm bằng Python code thuần (VD: tính tổng chi phí nên là hàm Python thuần, không cần LLM).
- Luôn giới hạn `recursion_limit` trong LangGraph graph run (mặc định ≤ 15) để tránh loop vô hạn tốn chi phí API.
- Log đầy đủ vào bảng `agent_logs`: input, output, input_tokens, output_tokens, duration_ms, agent_name (phục vụ Admin Dashboard + debug).

## 5. Quy tắc chung mọi ngôn ngữ
- Không magic number/string — khai báo hằng số `UPPER_SNAKE_CASE` có tên rõ nghĩa.
- Hàm nên < 50 dòng; nếu dài hơn, cân nhắc tách nhỏ.
- Xử lý lỗi rõ ràng (try/except có ý nghĩa), không nuốt lỗi im lặng (`except Exception: pass` là **cấm**).
- Không comment code chết — dùng Git history thay vì comment-out.
