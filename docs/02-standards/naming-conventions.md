# Naming Conventions

## 1. Biến & hàm (TypeScript — FE & BE)
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
| File khác (service, util, hook) | `kebab-case` hoặc `camelCase.ts` theo NestJS convention | `event.service.ts`, `useCreateEvent.ts` |

## 2. Database (PostgreSQL qua Prisma)
| Đối tượng | Style | Ví dụ |
|---|---|---|
| Tên bảng (model Prisma) | `PascalCase` số ít | `model Event`, `model PlanVote` |
| Tên bảng thực tế trong DB (map) | `snake_case` số nhiều | `@@map("events")`, `@@map("plan_votes")` |
| Tên cột | `camelCase` trong Prisma, map sang `snake_case` trong DB | `startDate` → `@map("start_date")` |
| Khoá ngoại | `<tên_bảng_số_ít>Id` | `eventId`, `userId` |
| Bảng trung gian (many-to-many) | ghép 2 tên bảng | `EventMember`, `PlanLocation` |
| Index | `idx_<bảng>_<cột>` | `idx_events_owner_id` |

## 3. API Endpoint & Route
- Xem chi tiết đầy đủ ở [api-design-guide.md](api-design-guide.md). Tóm tắt:
  - Danh từ số nhiều, `kebab-case`: `/events`, `/plan-votes`, `/ai-agents/orchestrator`
  - Không dùng động từ trong URL (`/getEvent` ❌) — dùng đúng HTTP method (`GET /events/:id` ✅)

## 4. Biến môi trường (`.env`)
- **`UPPER_SNAKE_CASE`**, có tiền tố theo nhóm dịch vụ để dễ scan:
```
# Server
PORT=3000
NODE_ENV=development

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/travel_ai

# Redis
REDIS_URL=redis://localhost:6379

# Auth
JWT_ACCESS_SECRET=
JWT_REFRESH_SECRET=
JWT_ACCESS_EXPIRES_IN=15m
JWT_REFRESH_EXPIRES_IN=7d
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
FACEBOOK_APP_ID=
FACEBOOK_APP_SECRET=

# AI
ANTHROPIC_API_KEY=
AI_MODEL_DEFAULT=claude-sonnet-4-6
AI_MAX_TOKENS_PER_REQUEST=4096

# External APIs
GOOGLE_PLACES_API_KEY=
MAPBOX_ACCESS_TOKEN=
OPENWEATHER_API_KEY=

# Email
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASSWORD=
```
- Không bao giờ commit file `.env` thật — chỉ commit `.env.example` (xem file mẫu ở gốc `docs/.env.example`).
- Biến nhạy cảm (secret/key/password/token) **bắt buộc** nằm trong `.env`, không hardcode trong code dù là môi trường dev.

## 5. Git — tên branch/commit
- Xem riêng [branch-naming.md](../01-workflow/branch-naming.md) và [commit-convention.md](../01-workflow/commit-convention.md).

## 6. Tên miền phụ / Route Frontend
| Loại | Quy tắc | Ví dụ |
|---|---|---|
| Route page | `kebab-case`, danh từ | `/events`, `/events/:id/plan`, `/ai-chat` |
| Query param | `camelCase` | `?sortBy=startDate&page=1` |
| Tên subdomain (nếu tách service) | `kebab-case` | `api.<domain>.com`, `ai.<domain>.com` (nếu tách AI service riêng) |
