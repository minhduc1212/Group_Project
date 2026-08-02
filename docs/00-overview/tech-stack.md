# Tech Stack

Lựa chọn công nghệ ưu tiên: **quen thuộc với sinh viên, có tài liệu tốt, miễn phí/free-tier đủ dùng cho đồ án, và phù hợp với LangGraph/AI orchestration**.

## 1. Frontend
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Framework | **React 18 + Vite + TypeScript** | Dựng nhanh, HMR nhanh hơn CRA, TS giúp bắt lỗi sớm khi làm việc nhóm |
| State management | **Zustand** (nhẹ) hoặc **Redux Toolkit** (nếu state phức tạp) | Zustand đủ cho scope đồ án, ít boilerplate |
| Data fetching | **TanStack Query (React Query)** | Cache, refetch, loading/error state tự động — khớp với Nhóm 3 (API rate-limited) |
| UI Kit | **Tailwind CSS + shadcn/ui** | Tốc độ dựng UI nhanh, dễ đồng bộ design giữa nhiều người |
| Form | **React Hook Form + Zod** | Validate schema dùng chung được với backend (Zod) |
| Map | **Mapbox GL JS** hoặc **Google Maps JS SDK** | Theo Nhóm 3 |
| i18n | **react-i18next** | Cho Nhóm 7 |
| Realtime chat UI (Agent 9.7) | **Socket.IO client** hoặc **SSE** | Xem chi tiết ở AI Agent Architecture |

## 2. Backend
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Runtime | **Node.js 20 LTS + TypeScript** | Dùng chung ngôn ngữ FE/BE → dễ chia sẻ type (Zod schema, DTO) |
| Framework | **NestJS** | Kiến trúc module hoá rõ ràng, DI sẵn, phù hợp team nhiều người chia module theo Nhóm 1–7, có Guard/Interceptor tiện cho Auth & validate input trước khi vào AI Agent |
| ORM | **Prisma** | Schema-first, type-safe, migration dễ review trong PR |
| Database | **PostgreSQL** | Quan hệ rõ ràng (User–Event–Plan–Vote–Member), hỗ trợ JSONB cho dữ liệu agent linh hoạt |
| Cache | **Redis** | Cache kết quả API bên thứ 3 (Nhóm 3), lưu session/rate-limit |
| Queue (tuỳ chọn nếu có thời gian) | **BullMQ (Redis-based)** | Xử lý async cho Agent research/booking dài hơi, export PDF |
| Auth | **Passport.js (Google/Facebook OAuth2 strategy) + JWT (access + refresh token)** | Chuẩn công nghiệp, NestJS có module tích hợp sẵn |
| Validation | **class-validator / Zod** | Chặn input xấu trước khi vào AI Agent (chống prompt injection) |

## 3. AI Multi-Agent System (Nhóm 4)
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Orchestration | **LangGraph.js** (hoặc LangGraph Python nếu team AI mạnh Python hơn — xem lưu ý bên dưới) | Chuẩn cho multi-agent graph, có state machine, checkpoint, human-in-the-loop cho vote |
| LLM Provider | **DeepSeek API** (`deepseek-chat` cho hội thoại/action/function calling, `deepseek-reasoner` cho suy luận/phân giải xung đột phức tạp) | Chi phí tối ưu, hiệu năng tiệm cận các mô hình hàng đầu, lý tưởng cho lập luận (Reasoning) và agent |
| RAG (nếu cần, cho Agent research 9.5) | **pgvector** (extension của Postgres đã dùng sẵn) thay vì thêm vector DB riêng | Giảm 1 hệ thống phải quản lý |
| Prompt management | Lưu prompt dạng file `.md`/`.ts` versioned trong repo, không hardcode rải rác | Dễ review, dễ A/B test |

> **Lưu ý về ngôn ngữ AI Agent**: Nếu người phụ trách Nhóm 4 mạnh Python hơn, có thể tách AI service thành **Python (FastAPI + LangGraph Python)** chạy độc lập, giao tiếp với NestJS backend qua REST/gRPC nội bộ. Quyết định này cần chốt sớm (tuần 1) vì ảnh hưởng đến kiến trúc — ghi vào `03-architecture/ai-agent-architecture.md`.

## 4. External APIs (Nhóm 3)
| Nhu cầu | Lựa chọn |
|---|---|
| Địa điểm/khách sạn/nhà hàng | Google Places API |
| Thời tiết | OpenWeatherMap (free tier đủ dùng) |
| Bản đồ | Mapbox (free tier hào phóng hơn Google Maps cho sinh viên) |
| Tỷ giá | exchangerate-api.com hoặc Frankfurter (free, không cần key) |

## 5. Notification & Export (Nhóm 5)
| Nhu cầu | Lựa chọn |
|---|---|
| Email | Nodemailer + SMTP (Gmail cho dev) hoặc Resend/SendGrid free tier |
| Cron job | node-cron (đơn giản) hoặc BullMQ repeatable jobs nếu đã dùng Redis |
| Export PDF | Puppeteer (render HTML→PDF, linh hoạt hơn pdfkit cho layout lịch trình đẹp) |

## 6. DevOps / Hạ tầng
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Containerization | **Docker + docker-compose** | Đồng bộ môi trường dev giữa 6 người, tránh "chạy trên máy tôi thì được" |
| CI | **GitHub Actions** | Lint + test + build tự động khi mở PR |
| Hosting Frontend | **Vercel** | Deploy preview tự động theo PR, free |
| Hosting Backend | **Render / Railway** (free tier) hoặc VPS nếu cần | Đơn giản cho đồ án |
| Hosting AI Service (nếu tách riêng) | Cùng nền tảng với Backend | |
| Monitoring lỗi | **Sentry** (free tier) | |
| Quản lý secrets | GitHub Actions Secrets + `.env` (không commit) | Xem `05-security/security-guidelines.md` |

## 7. Testing
| Hạng mục | Lựa chọn |
|---|---|
| Backend unit/integration test | **Jest + Supertest** |
| Frontend unit test | **Vitest + React Testing Library** |
| E2E (nếu có thời gian) | **Playwright** |
| AI Agent test | Jest với mock LLM response (xem `02-standards/testing-guide.md`) |

## 8. Bảng tóm tắt theo vai trò
| Vai trò | Công nghệ chính cần nắm |
|---|---|
| Backend dev (Auth, Core CRUD) | NestJS, Prisma, PostgreSQL, JWT/OAuth2 |
| AI Engineer | LangGraph, DeepSeek API, prompt engineering, pgvector |
| Frontend dev | React, TanStack Query, Tailwind, Socket.IO |
| Cyber Security | Input validation, OWASP Top 10, prompt injection defense, secrets management, rate limiting |
| Integration dev (Nhóm 3) | Google Places/Mapbox/OpenWeather SDK, Redis cache |
| DevOps kiêm nhiệm | Docker, GitHub Actions |
