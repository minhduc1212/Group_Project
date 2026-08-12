# 🚢 Deployment Guide — Vercel (FE) + Render (BE)

> Chi tiết triển khai cho 2 task deploy: **TASK-118** (Frontend → Vercel, Sprint 1) và **TASK-216** (Backend → Render, Sprint 2), kiểm chứng cuối ở **TASK-414** (Sprint 4).
> Bảng stack tham chiếu: [tech-stack.md](../00-overview/tech-stack.md) mục 6.
> ⚠️ **Quy tắc bất biến**: không bao giờ commit `.env`/secret lên Git; toàn bộ secret đặt qua env của nền tảng.

## 1. Kiến trúc deploy

```
[GitHub] main ──merge──► CD workflow
    │  (preview: mỗi PR chạy 1 preview build riêng)
    ├── .github/workflows/cd-frontend.yml ──► Vercel (Frontend: Vite + React)
    └── .github/workflows/cd-backend.yml  ──► Render (Backend: FastAPI + Postgres + Redis)

Frontend (Vercel) ── gọi API qua VITE_API_BASE_URL ──► Backend (Render)
```

| Tầng | Nền tảng | Deploy | Cấu hình |
|---|---|---|---|
| Frontend | **Vercel** | `main` → Production, PR → Preview | `vercel.json` + `cd-frontend.yml` |
| Backend | **Render** | `main` → auto-deploy | `render.yaml` (Blueprint) + `Dockerfile.prod` |
| Database | **Render PostgreSQL 15** | managed | qua `render.yaml` |
| Cache | **Render Redis 7** | managed | qua `render.yaml` |

## 2. Frontend — Vercel (TASK-118)

### 2.1 `vercel.json`
```json
{
  "buildCommand": "pnpm build",
  "outputDirectory": "dist",
  "framework": "vite",
  "headers": [
    { "source": "/assets/(.*)", "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }] }
  ]
}
```

### 2.2 Biến môi trường theo env
| Env | `VITE_API_BASE_URL` | `VITE_USE_MOCK` | `VITE_MAPBOX_ACCESS_TOKEN` |
|---|---|---|---|
| Preview (mỗi PR) | Backend **staging** trên Render | `true` (hoặc staging URL) | token Mapbox dev |
| Production | Render domain production | `false` | token Mapbox prod |

> `VITE_*` được Vite **bundle vào bundle JS** → không chứa secret. Mapbox token là public-token (chỉ cho phép read styles), không phải secret key.

### 2.3 Luồng CD
1. Push PR → Vercel tự tạo **Preview URL** (hoặc qua `vercel deploy --prebuilt` trong `cd-frontend.yml`).
2. Merge `main` → build production, upload build, smoke test URL live (HTTP 200 + không lỗi runtime).

## 3. Backend — Render (TASK-216)

### 3.1 `render.yaml` (Blueprint — khai báo cả 3 service)
```yaml
services:
  - type: web
    name: tripmate-backend
    runtime: docker
    repo: https://github.com/minhduc1212/Group_Project
    dockerContext: ./backend
    plan: free
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: tripmate-db
          property: connectionString
      - key: REDIS_URL
        fromService:
          type: redis
          name: tripmate-redis
          property: connectionString
      # Các secret còn lại (SECRET_KEY, DEEPSEEK_API_KEY, ...) đặt thủ công trên dashboard Render
    healthCheckPath: /health
  - type: postgres
    name: tripmate-db
    plan: free
    databaseName: tripmate
    ipAllowList: []
  - type: redis
    name: tripmate-redis
    plan: free
    maxmemoryPolicy: noeviction
```

### 3.2 Migration khi deploy
Dùng **Start Command** của web service: `alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
(hoặc chạy trong entrypoint của `Dockerfile.prod`).

### 3.3 `Dockerfile.prod` — yêu cầu tối thiểu
- **Multi-stage**: stage build (Poetry cài deps) → stage runtime.
- **Non-root user**: tạo user `app` chạy uvicorn (tránh container chạy root).
- Không copy `.env`; đọc biến môi trường từ Render.

### 3.4 Smoke test sau deploy
```
curl -fsS https://<render-domain>/health   # → {"status":"ok"}
```
Kiểm tra CORS cho phép đúng domain Vercel (xem `backend/app/main.py` CORSMiddleware — TASK-116).

## 4. Kiểm chứng cuối cùng — TASK-414

Checklist trước demo cuối Sprint 4 (chạy end-to-end trên 2 URL production thật):
- [ ] `/health` trên Render trả green.
- [ ] Vercel domain load trang, không lỗi console runtime.
- [ ] Luồng đăng nhập → tạo event → tạo plan → xem expense chạy xuyên FE↔BE.
- [ ] SSL hợp lệ trên cả 2 domain; CORS đúng domain FE.
- [ ] Quét repo: không có `.env`, API key, secret hardcode (xem [security-guidelines.md](../05-security/security-guidelines.md)).
- [ ] Cấu hình Rate Limit + HTTPS redirect hoạt động trên production.

## 5. Rủi ro & phòng tránh

| Rủi ro | Phòng tránh |
|---|---|
| Build frontend pass local nhưng fail trên Vercel | Chạy đúng command trong `vercel.json` (`pnpm build`), Node version khớp |
| Render service sleep (free tier) | Dùng plan phù hợp / health check; chấp nhận cold start cho demo |
| Secret lộ qua build log | Không `echo` biến môi trường trong CD workflow; dùng GitHub Secrets + Render env |
| Migration chạy 2 lần gây lỗi | `alembic` tự track version; giữ `alembic_version` — không xóa file migration cũ |
