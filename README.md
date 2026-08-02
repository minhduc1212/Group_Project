# 📚 Web Lên Kế Hoạch Nhóm Tích Hợp AI Multi-Agent

Đây là bộ tài liệu chuẩn hóa cho dự án, dùng chung cho toàn team (6 người: Backend FastAPI, Frontend React, AI Engineer LangGraph Python, Cyber Security, cùng các vai trò kiêm nhiệm). Mọi thành viên **bắt buộc đọc** các mục `01-workflow` và `02-standards` trước khi push code đầu tiên.

## Mục lục

### 00 — Tổng quan
- [Project Overview](docs/00-overview/project-overview.md) — Mục tiêu, phạm vi, đối tượng người dùng
- [Danh Sách Tính Năng (42 features)](feature.md) — **Toàn bộ 42 tính năng được đánh số theo 7 nhóm**
- [Hướng Dẫn Vận Hành & Luồng (Explanation)](explain.md) — **Giải thích luồng hoạt động, ví dụ từng EventType (Travel, Dining, Entertainment...), DeepSeek API**
- [Tech Stack](docs/00-overview/tech-stack.md) — **Công nghệ sử dụng: Python FastAPI, LangGraph Python, React, Postgres, Redis, DeepSeek API**
- [Team & Roles](docs/00-overview/team-roles.md) — **Chia 6 người theo vai trò để làm song song** (không chia theo nhóm tính năng), ma trận RACI

### 01 — Quy trình làm việc (Workflow)
- [Contract-First Workflow](docs/01-workflow/contract-first-workflow.md) — **Cơ chế cốt lõi để 6 người chạy song song** không bị block nhau (đọc trước tiên)
- [Cross-Team Collaboration](docs/01-workflow/cross-team-collaboration.md) — **Thêm tính năng giữa chừng & nhảy vào code của nhau không conflict**
- [Git Workflow](docs/01-workflow/git-workflow.md) — Mô hình branching, quy trình từ task → PR → merge
- [Branch Naming](docs/01-workflow/branch-naming.md) — Quy tắc đặt tên nhánh
- [Commit Convention](docs/01-workflow/commit-convention.md) — Conventional Commits
- [Code Review Checklist](docs/01-workflow/code-review-checklist.md) — Checklist review PR

### 02 — Tiêu chuẩn kỹ thuật (Standards)
- [Coding Conventions](docs/02-standards/coding-conventions.md) — **Style code Python FastAPI (Ruff/Black/Pydantic v2) / Frontend (React/TS)**
- [Naming Conventions](docs/02-standards/naming-conventions.md) — Đặt tên biến, hàm, class, file, DB, env
- [API Design Guide](docs/02-standards/api-design-guide.md) — Chuẩn REST endpoint, domain, versioning (FastAPI `/docs`)
- [Documentation Guide](docs/02-standards/documentation-guide.md) — Quy định viết docs, README, Docstring
- [Testing Guide](docs/02-standards/testing-guide.md) — Chuẩn viết Unit Test / Integration Test (Pytest / Vitest)

### 03 — Kiến trúc hệ thống (Architecture)
- [System Architecture](docs/03-architecture/system-architecture.md) — Sơ đồ tổng thể hệ thống (FastAPI Backend + LangGraph Python)
- [Database Schema](docs/03-architecture/database-schema.md) — Thiết kế bảng dữ liệu chính (SQLAlchemy / SQLModel / Prisma, EventType, StopCategory, Invitation, metadata JSON)
- [AI Agent Architecture](docs/03-architecture/ai-agent-architecture.md) — Kiến trúc Multi-Agent (LangGraph Python, EventType routing, DeepSeek API)

### 04 — Phân chia công việc (Tasks) — chia theo **người**, chạy song song
- [Task Board tổng](docs/04-tasks/task-board.md) — Bảng theo dõi tiến độ + Sprint plan 6 track song song
- [Person 1 — Backend Dev A (Core Domain: Auth + Event/Plan/Vote/Invitation - FastAPI)](docs/04-tasks/person-1-backend-core.md)
- [Person 2 — Backend Dev B (Platform: External API + Notification/Export + Admin - FastAPI)](docs/04-tasks/person-2-backend-platform.md)
- [Person 3 — AI Engineer (Multi-Agent System & DeepSeek API - LangGraph Python)](docs/04-tasks/person-3-ai-engineer.md)
- [Person 4 — Frontend Dev A (Core Flows UI)](docs/04-tasks/person-4-frontend-core.md)
- [Person 5 — Frontend Dev B (AI Experience & Growth UI)](docs/04-tasks/person-5-frontend-growth.md)
- [Person 6 — Cyber Security & DevOps (FastAPI Security, Docker, Ruff, Pytest)](docs/04-tasks/person-6-security-devops.md)

### 05 — Bảo mật (Security)
- [Security Guidelines](docs/05-security/security-guidelines.md) — Checklist bảo mật, prompt injection defense, Pydantic validation, secrets management

### Khác
- [CONTRIBUTING.md](CONTRIBUTING.md) — Hướng dẫn đóng góp code (tóm tắt nhanh cho người mới)
- [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) — Template PR
- [.env.example](.env.example) — Mẫu biến môi trường chuẩn (bao gồm FastAPI & DeepSeek API settings)

---

## Cách sử dụng bộ docs này

1. Người mới vào team → đọc `CONTRIBUTING.md` (5 phút) → đọc `feature.md` & `explain.md` → đọc file task nhóm mình phụ trách trong `04-tasks`.
2. Trước khi code → đọc `02-standards` liên quan (coding convention Python FastAPI / React).
3. Trước khi mở PR → check `docs/01-workflow/code-review-checklist.md`.
4. Khi thêm tính năng mới ảnh hưởng kiến trúc → cập nhật `docs/03-architecture` trong cùng PR (docs-as-code, không để lệch thực tế).

> **Nguyên tắc**: Code và docs sống chung một chỗ (tài liệu nằm trong `/docs` trong repo), thay đổi kiến trúc/API luôn đi kèm cập nhật doc tương ứng trong PR. PR thiếu doc cập nhật sẽ bị reject ở review.
