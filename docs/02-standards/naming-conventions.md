# Naming Conventions

## 1. Biến & hàm (TypeScript — FE)
| Đối tượng | Style | Ví dụ |
|---|---|---|
| Biến, tham số | `camelCase` | `userId`, `eventStartDate` |
| Hàm | `camelCase`, động từ đầu | `createEvent()`, `getPlanById()`, `isOwner()` |
| Boolean | tiền tố `is/has/can/should` | `isOwner`, `hasVoted`, `canEditPlan` |
| Class, Interface, Type | `PascalCase` | `EventService`, `CreatePlanDto`, `AgentContext` |
| Interface (không tiền tố `I`) | `PascalCase` thường | `User` không phải `IUser` (theo chuẩn TS hiện đại) |
| Enum | `PascalCase` tên, `UPPER_CASE` giá trị | `enum EventRole { OWNER = 'OWNER', MEMBER = 'MEMBER', VIEWER = 'VIEWER' }` |
| Hằng số toàn cục | `UPPER_SNAKE_CASE` | `MAX_MEMBERS_PER_EVENT`, `DEFAULT_CACHE_TTL_SECONDS` |
| File component React | `PascalCase.tsx` | `EventCard.tsx`, `PlanTimeline.tsx` |
| File khác (service, util, hook) | `kebab-case` hoặc `camelCase.ts` | `event.service.ts`, `useCreateEvent.ts` |

## 2. Database (PostgreSQL qua SQLAlchemy / SQLModel)
| Đối tượng | Style | Ví dụ |
|---|---|---|
| Tên model SQLAlchemy | `PascalCase` số ít | `class Event(Base)`, `class PlanVote(Base)` |
| Tên bảng thực tế trong DB (`__tablename__`) | `snake_case` số nhiều | `"events"`, `"plan_votes"` |
| Tên cột (SQLAlchemy attribute) | `snake_case` | `start_date`, `created_by_id` |
| Khoá ngoại | `<tên_bảng_số_ít>_id` | `event_id`, `user_id` |
| Bảng trung gian (many-to-many) | ghép 2 tên bảng | `EventMember`, `PlanLocation` |
| Index | `idx_<bảng>_<cột>` | `idx_events_owner_id` |

## 3. API Endpoint & Route
- Xem chi tiết đầy đủ ở [api-design-guide.md](api-design-guide.md). Tóm tắt:
  - Danh từ số nhiều, `kebab-case`: `/events`, `/plan-votes`, `/ai-agents/orchestrator`
  - Không dùng động từ trong URL (`/getEvent` ❌) — dùng đúng HTTP method (`GET /events/{id}` ✅)

## 4. Biến môi trường (`.env`)
- **`UPPER_SNAKE_CASE`**, có tiền tố theo nhóm dịch vụ để dễ scan:
```
# Server
PORT=8000
PROJECT_NAME=Web_Len_Ke_Hoach_Nhom_AI
ENVIRONMENT=development
FRONTEND_URL=http://localhost:5173

# Database
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/tripmate

# Redis
REDIS_URL=redis://localhost:6379/0

# Auth (JWT & OAuth2)
SECRET_KEY=change-me-super-secret-key-32-chars-min
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_CALLBACK_URL=http://localhost:8000/api/v1/auth/google/callback
FACEBOOK_APP_ID=
FACEBOOK_APP_SECRET=

# AI (DeepSeek API)
DEEPSEEK_API_KEY=
AI_MODEL_DEFAULT=deepseek-chat
AI_MODEL_REASONING=deepseek-reasoner
AI_MAX_TOKENS_PER_REQUEST=4096
AI_MAX_STEPS_PER_SESSION=15

# External APIs
GOOGLE_PLACES_API_KEY=
MAPBOX_ACCESS_TOKEN=
OPENWEATHER_API_KEY=
EXCHANGE_RATE_API_KEY=

# Email (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=
SMTP_PASSWORD=
EMAILS_FROM_EMAIL=no-reply@tripmate.com
EMAILS_FROM_NAME=TripMate AI

# Rate Limit
RATE_LIMIT_AI_PER_MINUTE=20
RATE_LIMIT_AUTH_PER_MINUTE=10

# Frontend (Vite) — tiền tố VITE_* được Vite bundle vào code FE, KHÔNG chứa secret
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_USE_MOCK=true
VITE_MAPBOX_ACCESS_TOKEN=
VITE_APP_URL=http://localhost:5173
```
- Không bao giờ commit file `.env` thật — chỉ commit `.env.example` (xem file mẫu ở thư mục gốc repo: `.env.example`).
- Biến nhạy cảm (secret/key/password/token) **bắt buộc** nằm trong `.env`, không hardcode trong code dù là môi trường dev.

## 5. Git — tên branch/commit
- Xem riêng [branch-naming.md](../01-workflow/branch-naming.md) và [commit-convention.md](../01-workflow/commit-convention.md).

## 6. Tên miền phụ / Route Frontend
| Loại | Quy tắc | Ví dụ |
|---|---|---|
| Route page | `kebab-case`, danh từ | `/events`, `/events/{id}/plan`, `/ai-chat` |
| Query param | `camelCase` | `?sortBy=startDate&page=1` |
| Tên subdomain (nếu tách service) | `kebab-case` | `api.<domain>.com`, `ai.<domain>.com` (nếu tách AI service riêng) |
