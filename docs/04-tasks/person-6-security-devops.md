# Person 6 — Cyber Security & DevOps

**Sở hữu**: Hạ tầng CI/CD, Docker, bảo mật xuyên suốt toàn dự án. Có backlog riêng chạy song song từ ngày 1 — **không ngồi chờ có code mới bắt đầu việc**.

## Sprint 0 — Contract & hạ tầng nền (Python FastAPI + Docker)
- [ ] Dựng `docker-compose.yml` (FastAPI / Uvicorn, Postgres, Redis) — mọi người cần dùng ngay ngày 1
- [ ] Setup GitHub Actions CI: Ruff (lint) → Pytest → Docker build, branch protection rule cho `main`
- [ ] Setup Husky + pre-commit hook (chạy Ruff, Black, Mypy)
- [ ] Viết threat model sơ bộ cho hệ thống (đặc biệt luồng AI Agent) dựa trên kiến trúc đã chốt ở Sprint 0
- [ ] Review & góp ý FastAPI OpenAPI contract dưới góc độ bảo mật (endpoint nào cần rate limit, cần Dependency Security gì)

## Sprint 1 — Review Auth + siết bảo mật nền tảng
- [ ] Review toàn bộ PR Auth (Backend Dev A) theo checklist `05-security/security-guidelines.md` mục 6
- [ ] Cấu hình FastAPI `CORSMiddleware` với domain cụ thể (không `*`), `TrustedHostMiddleware`
- [ ] Setup rate limiting (FastAPI Limiter / Slowapi / Redis) cho endpoint auth
- [ ] Setup quản lý secrets: GitHub Actions Secrets, Pydantic `BaseSettings`, kiểm tra `.gitignore` chặn `.env` từ commit đầu tiên
- [ ] Setup Dependabot / `pip audit` tự động trong CI

## Sprint 2 — Review Integration & chuẩn bị AI
- [ ] Review PR External API (Backend Dev B): kiểm tra timeout/retry (`httpx`), không lộ secret key phía Frontend
- [ ] Viết chi tiết checklist chống prompt injection cụ thể cho AI Engineer áp dụng (dựa trên threat model Sprint 0)
- [ ] Setup Sentry Python SDK (theo dõi lỗi runtime)

## Sprint 3 — Review AI Agent (trọng tâm bảo mật)
- [ ] Review kỹ input validation/sanitize bằng Pydantic & bleach trước khi vào prompt (AI Engineer)
- [ ] Review Pydantic schema validate output LLM trước khi lưu DB
- [ ] Test thử các kịch bản prompt injection cơ bản trên môi trường dev (không phá hệ thống thật)
- [ ] Kiểm tra rate limit `/api/v1/ai/*` hoạt động đúng

## Sprint 4 — Pentest & hoàn thiện
- [ ] Pentest toàn hệ thống trước demo: thử các lỗi OWASP Top 10 cơ bản (injection, broken auth, broken access control, XSS)
- [ ] Kiểm tra Admin Dashboard không lộ dữ liệu nhạy cảm
- [ ] Review toàn bộ `.env.example` khớp với biến thật đang dùng, không sót secret nào bị hardcode
- [ ] Tổng hợp báo cáo bảo mật ngắn gọn cho buổi demo/nộp đồ án

## Định nghĩa Done chung
- Mọi PR động vào Auth/AI/Admin có sign-off của Security trước khi merge
- CI luôn xanh, branch `main` được bảo vệ đúng cấu hình

## Không được tự ý làm khi chưa báo
- Đổi rate limit/CORS config ảnh hưởng nhiều người đang test → báo `#dev` trước khi đổi ở môi trường chung (staging).
