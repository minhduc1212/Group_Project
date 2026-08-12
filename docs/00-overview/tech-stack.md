# Tech Stack

Lựa chọn công nghệ ưu tiên: **Python FastAPI cho Backend & AI Agent (đồng bộ 100% sinh thái LangGraph), React cho Frontend, PostgreSQL, Redis, và DeepSeek API**.

## 1. Frontend
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Framework | **React 18 + Vite + TypeScript** | Dựng nhanh, HMR nhanh hơn CRA, TS giúp bắt lỗi sớm khi làm việc nhóm |
| State management | **Zustand** (nhẹ) hoặc **Redux Toolkit** (nếu state phức tạp) | Zustand đủ cho scope đồ án, ít boilerplate |
| Data fetching | **TanStack Query (React Query)** | Cache, refetch, loading/error state tự động — khớp với Nhóm 3 (API rate-limited) |
| UI Kit | **Tailwind CSS + shadcn/ui** | Tốc độ dựng UI nhanh, dễ đồng bộ design giữa nhiều người |
| Form | **React Hook Form + Zod** | Validate schema UI client trước khi submit |
| Map | **Mapbox GL JS** hoặc **Google Maps JS SDK** | Theo Nhóm 3 |
| i18n | **react-i18next** | Cho Nhóm 7 |
| Realtime chat UI (Agent 9.7) | **WebSockets / SSE (FastAPI EventSourceResponse)** | Tích hợp sẵn trong FastAPI mượt mà |

## 2. Backend (Python FastAPI)
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Runtime | **Python 3.11+** | Cùng hệ sinh thái với AI/LangGraph → không cần tách 2 ngôn ngữ Node/Python |
| Framework | **FastAPI** | Tốc độ cao (ASGI/uvicorn), tự động sinh OpenAPI/Swagger doc (`/docs`), Pydantic v2 validation native, async native |
| ORM | **SQLAlchemy 2.0 (Async) / SQLModel** | Type-safe, hỗ trợ async/await với PostgreSQL, tích hợp Pydantic mượt mà |
| Migration | **Alembic** | Thư viện migration tiêu chuẩn của Python SQLAlchemy |
| Database | **PostgreSQL (asyncpg driver)** | Hỗ trợ quan hệ rõ ràng, JSONB cho metadata linh hoạt, pgvector cho RAG |
| Cache | **Redis (redis-py async)** | Cache kết quả API bên thứ 3 (Nhóm 3), lưu session/rate-limit |
| Queue / Background | **Celery / Arq / FastAPI BackgroundTasks** | Xử lý async cho Agent research, gửi email, export PDF |
| Auth | **FastAPI Security + PyJWT + Passlib (bcrypt)** | Chuẩn OAuth2 (Google/Facebook SDK) + JWT access/refresh token |
| Validation | **Pydantic v2** | Chặn input xấu, validate Zod/Pydantic schema trước khi vào AI Agent |

## 3. AI Multi-Agent System (Nhóm 4)
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Orchestration | **LangGraph Python (`langgraph`)** | Thư viện gốc của LangChain cho multi-agent graph, state machine, checkpointing, human-in-the-loop |
| LLM Provider | **DeepSeek API** (`deepseek-chat` cho hội thoại/action/function calling, `deepseek-reasoner` cho suy luận/phân giải xung đột phức tạp) | Chi phí tối ưu, hiệu năng tiệm cận các mô hình hàng đầu |
| Integration | **LangChain DeepSeek (`langchain-deepseek`)** / OpenAIChat | Chạy trực tiếp trong Python Backend mà không cần IPC/gRPC cross-language |
| RAG (nếu cần) | **pgvector-python** | Tích hợp sẵn trong PostgreSQL |
| Prompt management | File `.py`/`.md` versioned trong repo | Dễ review, dễ test |

## 4. External APIs (Nhóm 3)
| Nhu cầu | Lựa chọn |
|---|---|
| Địa điểm/khách sạn/nhà hàng | Google Places API (httpx async) |
| Thời tiết | OpenWeatherMap (free tier) |
| Bản đồ | Mapbox |
| Tỷ giá | exchangerate-api.com / Frankfurter |

## 5. Notification & Export (Nhóm 5)
| Nhu cầu | Lựa chọn |
|---|---|
| Email | FastAPI-Mail / aiosmtplib (SMTP async) |
| Cron job | APScheduler / Celery Beat |
| Export PDF | WeasyPrint / ReportLab / Playeteer Python |

## 6. DevOps / Hạ tầng
| Hạng mục | Lựa chọn | Lý do |
|---|---|---|
| Containerization | **Docker + docker-compose** | Uvicorn + PostgreSQL + Redis local |
| Package Manager | **Poetry / uv** | Quản lý dependency Python sạch sẽ |
| CI | **GitHub Actions** | Ruff (lint) + pytest + build |
| CD (Frontend) | **GitHub Actions + Vercel** | Deploy tự động: mỗi PR → Preview URL, merge `main` → Production (TASK-118) |
| CD (Backend) | **GitHub Actions + Render Blueprint** | `render.yaml` + `Dockerfile.prod`: auto-deploy FastAPI + Postgres 15 + Redis 7 khi merge `main` (TASK-216) |
| Hosting Frontend | **Vercel** | Free preview + production domain |
| Hosting Backend | **Render** (fallback: Railway / VPS) | Chạy FastAPI uvicorn server |
| Quản lý secrets | `.env` + Pydantic BaseSettings | Production: đặt qua env của Vercel/Render, không commit `.env` |
| Deploy guide | [deployment-guide.md](../03-architecture/deployment-guide.md) | Chi tiết `vercel.json`, `render.yaml`, smoke test |

## 7. Testing
| Hạng mục | Lựa chọn |
|---|---|
| Backend unit/integration test | **Pytest + HTTPX AsyncClient** |
| Frontend unit test | **Vitest + React Testing Library** |
| AI Agent test | Pytest với mock LLM response |

## 8. Bảng tóm tắt theo vai trò
| Vai trò | Công nghệ chính cần nắm |
|---|---|
| Backend dev (Auth, Core CRUD) | Python 3.11+, FastAPI, SQLAlchemy/SQLModel, Pydantic, PyJWT, Alembic |
| AI Engineer | Python 3.11+, LangGraph Python, DeepSeek API, langchain-deepseek |
| Frontend dev | React 18, TypeScript, TanStack Query, Tailwind CSS, WebSocket |
| Cyber Security | FastAPI Security, OWASP Top 10, Pydantic sanitization, rate limiting, secrets management |
| Integration dev (Nhóm 3) | HTTPX async, Google Places API, Redis async (redis-py) |
| DevOps kiêm nhiệm | Docker, GitHub Actions, Ruff, Poetry/uv |
