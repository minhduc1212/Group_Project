# Contributing Guide

Chào mừng vào team! Đọc [guides.md](guides.md) (15 phút) để xem lộ trình đọc tài liệu theo vai trò của bạn trước khi mở PR đầu tiên.

## Bắt đầu nhanh
```bash
git clone <repo-url>
cd Group_Project

# --- Backend (Python FastAPI) ---
cd backend
cp ../.env.example .env    # .env.example nằm ở root repo — copy vào backend/.env và điền key
docker compose up -d        # chạy PostgreSQL + Redis local
poetry install              # hoặc: pip install -r requirements.txt
poetry run alembic upgrade head
poetry run uvicorn app.main:app --reload --port 8000

# --- Frontend (React + Vite) ---
cd ../frontend
pnpm install
pnpm run dev
```

## Quy trình làm việc (tóm tắt — chi tiết ở `docs/01-workflow/`)
1. Nhận task từ [task-board.md](docs/04-tasks/task-board.md), tự gán mình, chuyển `In Progress`.
2. Tạo branch: `git checkout -b feature/n<x>-mo-ta-ngan` (xem [branch-naming.md](docs/01-workflow/branch-naming.md)).
3. Code theo chuẩn ở [coding-conventions.md](docs/02-standards/coding-conventions.md) và [naming-conventions.md](docs/02-standards/naming-conventions.md).
4. Viết test theo [testing-guide.md](docs/02-standards/testing-guide.md), chạy `ruff check . && pytest` trước khi push.
5. Cập nhật tài liệu theo [post-task-documentation.md](docs/01-workflow/post-task-documentation.md) (API spec, DB schema, ADR, tick `[x]` task board).
6. Commit theo [commit-convention.md](docs/01-workflow/commit-convention.md).
7. Mở PR bằng template, điền mục Updated Docs, xin review theo [code-review-checklist.md](docs/01-workflow/code-review-checklist.md).
8. Merge bằng **Squash and merge** sau khi có ít nhất 1 approve + CI xanh + Docs đầy đủ.

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

## Quy trình bàn giao công việc (Handover Workflow)
Xem hướng dẫn chi tiết ở [cross-team-collaboration.md](docs/01-workflow/cross-team-collaboration.md#phần-3-quy-trình-bàn-giao-công-việc-task-handover-workflow), gồm 4 trường hợp:
1. **Bàn giao khi xong task**: Self-check, cập nhật tick `[x]` trên file task & `docs/TASKS.md`, mở PR & báo kênh `#dev`.
2. **Bàn giao khi nhờ người khác làm hộ**: Push branch `feature/TASK-xxx-wip`, để lại Handover Note trên PR/Issue, đổi Assignee.
3. **Bàn giao khi bị Blocked**: Đổi trạng thái `🔴 Blocked` trên board, báo chi tiết trên `#contract-changes` kèm tag người phụ trách.
4. **Bàn giao mốc Sprint (Integration Day)**: Tắt mock, test luồng thật, demo 15p, Security sign-off.

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
