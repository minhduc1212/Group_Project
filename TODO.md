# 📋 TODO & Phân Công Nhân Sự (Project Roles & Task Assignment)

## 🌐 External APIs Tích Hợp
- **Map & Places API**: Tra cứu địa điểm (Google Places API / Mapbox), lọc theo `StopCategory` (RESTAURANT, CAFE, ENTERTAINMENT, ATTRACTION, HOTEL)
- **Khách sạn (Hotel API)**: So sánh giá phòng, đánh giá, tiện ích và lấy link đặt phòng trực tiếp
- **Thời tiết (Weather API)**: Dự báo thời tiết OpenWeatherMap theo tọa độ địa điểm

---

## 👥 Phân Công Vai Trò & Nhân Sự (6 Thành Viên)

### 1. Backend (3 người)
- **Tạ Quang Huy** (Lead Backend Dev A): Thiết kế DB Schema SQLAlchemy, Auth API (JWT/OAuth), Event/Plan/Vote/Invitation CRUD, RolesGuard & Tích hợp AI Agent Tooling
- **Hà Đăng Huy** (Backend Dev B): External APIs (Google Places, OpenWeatherMap, Currency Converter) & Redis Caching Service
- **Phạm Đình Ánh Dương** (Backend Dev C): Realtime WebSockets/SSE Server, Email Notifications (SMTP), Export PDF (WeasyPrint), Admin Statistics APIs

### 2. Frontend (2 người)
- **Hà Đăng Huy** (Frontend Dev A - Core UI): UI Kit Setup, Auth UI, Event Dashboard, EventType Selector, Manual Plan Builder, Vote UI & Mapbox Integration
- **Nguyễn Minh Đức** (Frontend Dev B - AI & Growth UI): Realtime AI Streaming Chat UI, Landing Page, i18n (VI/EN), Checklist UI, Shared Expenses Calculator, Admin Dashboard UI

### 3. AI Agent (2 người)
- **Nguyễn Tùng Dương** (AI Lead): LangGraph Multi-Agent Architecture, State Management, Orchestrator Agent, DeepSeek V3/R1 integration (Plan Agent reasoning, Cost Agent, Conflict Resolver)
- **Tạ Quang Huy** (AI Integration Engineer): Bridge Tool Calling між AI Agent và External APIs (Places/Weather/Hotels), Mock Fixtures Data

### 4. DevOps & Security (1 người)
- **Đinh Tiến Luân** (DevOps & Security Engineer): Docker Compose setup, CI/CD GitHub Actions pipeline, Pre-commit hooks & Ruff/Black linter, FastAPI Security Middlewares, Input/Output Sanitization Audit, Pentest OWASP Top 10

---

## 🔗 Liên Kết Tài Liệu
- [Team & Roles Detailed](team-roles.md) — Chi tiết vai trò & ma trận RACI
- [Master Task Board](docs/04-tasks/task-board.md) — Tiến độ tổng 6 track
- [Master Detailed Task Breakdown](docs/TASKS.md) — Danh sách micro-tasks chi tiết cho từng file
