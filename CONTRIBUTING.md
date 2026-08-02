# Contributing Guide

Chào mừng vào team! Đọc file này (5 phút) trước khi mở PR đầu tiên.

## Bắt đầu nhanh
```bash
git clone <repo-url>
cd travel-ai

# --- Backend (Python FastAPI) ---
cd backend
cp .env.example .env       # điền các key cần thiết
docker compose up -d        # chạy PostgreSQL + Redis local
poetry install              # hoặc: pip install -r requirements.txt
poetry run alembic upgrade head
poetry run uvicorn app.main:app --reload --port 8000

# --- Frontend (React + Vite) ---
cd ../frontend
npm install
npm run dev
```

## Quy trình làm việc (tóm tắt — chi tiết ở `docs/01-workflow/`)
1. Nhận task từ [task-board.md](docs/04-tasks/task-board.md), tự gán mình, chuyển `In Progress`.
2. Tạo branch: `git checkout -b feature/n<x>-mo-ta-ngan` (xem [branch-naming.md](docs/01-workflow/branch-naming.md)).
3. Code theo chuẩn ở [coding-conventions.md](docs/02-standards/coding-conventions.md) và [naming-conventions.md](docs/02-standards/naming-conventions.md).
4. Viết test theo [testing-guide.md](docs/02-standards/testing-guide.md), chạy `ruff check . && pytest` trước khi push.
5. Commit theo [commit-convention.md](docs/01-workflow/commit-convention.md).
6. Mở PR bằng template, xin review theo [code-review-checklist.md](docs/01-workflow/code-review-checklist.md).
7. Merge bằng **Squash and merge** sau khi có ít nhất 1 approve + CI xanh.

## Muốn thêm tính năng mới giữa chừng?
Xem quy trình chi tiết ở [cross-team-collaboration.md](docs/01-workflow/cross-team-collaboration.md), tóm tắt nhanh:
- **Nhỏ** (trong module mình) → Làm luôn, PR bình thường.
- **Trung bình** (đổi API/schema) → Báo `#contract-changes` → PR cập nhật docs trước → rồi code.
- **Lớn** (tính năng hoàn toàn mới) → Mở Issue **Feature Proposal** → weekly sync → phân công.

## Muốn nhảy vào giúp người khác?
Xem hướng dẫn chi tiết ở [cross-team-collaboration.md](docs/01-workflow/cross-team-collaboration.md), tóm tắt nhanh:
1. Nhặt task nhỏ (vertical slice) từ board — mỗi task có Acceptance Criteria rõ ràng.
2. Báo người phụ trách trên kênh `#dev`.
3. Đọc file task + schema liên quan.
4. Code trong đúng module, đúng convention.
5. PR tag chủ module làm reviewer.

## Việc tuyệt đối không làm
- ❌ Push trực tiếp lên `main`
- ❌ Commit file `.env` hoặc bất kỳ secret/API key nào
- ❌ Merge PR khi CI fail hoặc còn comment `[blocking]` chưa resolve
- ❌ Đổi DB models mà không báo AI Engineer + Integration Dev
- ❌ Sửa code bên trong module của người khác mà không báo trước
- ❌ Để AI Agent tự chốt hành động không thể đảo ngược mà không qua xác nhận người dùng (xem `docs/05-security/security-guidelines.md`)

## Cần giúp đỡ?
- Câu hỏi kỹ thuật chung → kênh `#dev`
- Vấn đề bảo mật khẩn → tag `@security` trực tiếp, không đợi daily standup
- Muốn đề xuất tính năng mới → mở Issue Feature Proposal (xem [cross-team-collaboration.md](docs/01-workflow/cross-team-collaboration.md))
- Không rõ task/acceptance criteria → hỏi người có "A" trong RACI ở [team-roles.md](docs/00-overview/team-roles.md) trước khi tự đoán và code sai hướng

## Bản đồ tài liệu đầy đủ
Xem [README.md](README.md) để có mục lục toàn bộ docs.
