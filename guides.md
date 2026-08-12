# 🗺️ Hướng Dẫn Bắt Đầu & Lộ Trình Đọc Tài Liệu (guides.md)

Chào mừng bạn đến với dự án **Web Lên Kế Hoạch Nhóm Tích Hợp AI Multi-Agent**! 

Dự án có bộ tài liệu đầy đủ và chuẩn hóa. Nếu bạn mới vào team hoặc lần đầu xem repo, **đừng đọc hết tất cả cùng lúc**. Hãy làm theo hướng dẫn dưới đây để biết chính xác cần đọc gì theo vai trò của mình và thực hiện theo từng bước.

---

## 🧭 1. Bạn Là Ai? Chọn Lộ Trình Đọc Docs (15 Phút)

### 🅰️ Giám Khảo / Mentor / Người Xem Dự Án (Reviewer & Evaluator)
> **Mục tiêu**: Hiểu nhanh dự án làm gì, độ phức tạp kỹ thuật ra sao, tính năng có gì hay.

1. Đọc **[README.md](README.md)** (2 phút) — Tổng quan mục lục và định hướng.
2. Đọc **[feature.md](feature.md)** (3 phút) — Xem danh sách 42 tính năng phân theo 7 nhóm.
3. Đọc **[explain.md](explain.md)** (5 phút) — Xem các luồng chạy thực tế (`TRAVEL`, `DINING`, `ENTERTAINMENT`...) và cách dùng DeepSeek API.
4. Đọc **[system-architecture.md](docs/03-architecture/system-architecture.md)** (3 phút) — Xem sơ đồ tổng thể Python FastAPI + React + Redis + Postgres + LangGraph.
5. Đọc **[TASKS.md](docs/TASKS.md)** (2 phút) — Xem bảng phân rã task chi tiết đến từng file.

---

### 🅱️ Backend Dev A — Core Domain & AI Integration (Tạ Quang Huy)
> **Mục tiêu**: Nắm DB schema, API spec, Auth, Event/Plan/Vote/Invitation và Tool Calling cho AI Agent.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Hiểu cơ chế code song song từ ngày 1 bằng API contract.
2. Đọc **[database-schema.md](docs/03-architecture/database-schema.md)** (5 phút) — Nắm kỹ các model SQLAlchemy: User, Event, Plan, PlanStop, PlanVote, Invitation.
3. Đọc **[api-design-guide.md](docs/02-standards/api-design-guide.md)** (3 phút) — Nắm các endpoint REST `/auth/*`, `/events/*`, `/invitations/*`, `/plans/*`, `/votes/*`.
4. Mở **[person-1-backend-core.md](docs/04-tasks/person-1-backend-core.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` phụ trách.

---

### 🅲️ Backend Dev B & C — Platform & Integration (Hà Đăng Huy & Phạm Đình Ánh Dương)
> **Mục tiêu**: Nắm cách tích hợp Google Places, Weather, Currency, Redis cache (Hà Đăng Huy) và Email SMTP, PDF Export, Realtime WS/SSE Server, Admin APIs (Phạm Đình Ánh Dương).

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Hiểu cách trả API spec để AI Engineer và FE dùng.
2. Đọc **[api-design-guide.md](docs/02-standards/api-design-guide.md)** (3 phút) — Xem endpoint `/places/*`, `/weather`, `/export/*`, `/admin/*`.
3. Đọc **[system-architecture.md](docs/03-architecture/system-architecture.md)** (3 phút) — Nắm cơ chế Redis Caching cho External APIs và WebSocket/SSE setup.
4. Mở **[person-2-backend-platform.md](docs/04-tasks/person-2-backend-platform.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` phụ trách.

---

### 🅳️ AI Agent Team — LangGraph & Integration (Nguyễn Tùng Dương & Tạ Quang Huy)
> **Mục tiêu**: Hiểu cấu trúc Agent graph, EventType routing, DeepSeek V3/R1 models (Nguyễn Tùng Dương) và AI Tool Calling / Mock Fixtures (Tạ Quang Huy).

1. Đọc **[ai-agent-architecture.md](docs/03-architecture/ai-agent-architecture.md)** (7 phút) — Nắm mô hình Orchestrator-Worker, routing 6 EventType, LangGraph Python state.
2. Đọc **[explain.md](explain.md)** (5 phút) — Nắm sự phối hợp giữa `deepseek-chat` (V3) và `deepseek-reasoner` (R1).
3. Đọc **[database-schema.md](docs/03-architecture/database-schema.md)** (3 phút) — Nắm field `category` và `metadata` JSON của `PlanStop`.
4. Mở **[person-3-ai-engineer.md](docs/04-tasks/person-3-ai-engineer.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` phụ trách.

---

### 🅴️ Frontend Dev A — Core Flows UI (Hà Đăng Huy)
> **Mục tiêu**: Nắm UI mockup, MSW mock setup, các màn hình Auth, Event Dashboard, Plan Builder, Voting & Mapbox.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Hiểu cách dùng MSW mock API response để code UI ngay từ ngày 1.
2. Đọc **[api-design-guide.md](docs/02-standards/api-design-guide.md)** (3 phút) — Nắm shape dữ liệu trả về từ API.
3. Đọc **[coding-conventions.md](docs/02-standards/coding-conventions.md)** (3 phút) — Chuẩn React, TypeScript, TanStack Query, Tailwind.
4. Mở **[person-4-frontend-core.md](docs/04-tasks/person-4-frontend-core.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` phụ trách.

---

### 🅵️ Frontend Dev B — AI Experience & Growth UI (Nguyễn Minh Đức)
> **Mục tiêu**: Nắm UI Chat AI streaming, Landing Page, đa ngôn ngữ (i18n), Checklist UI, Shared Expenses và Admin Dashboard UI.

1. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (5 phút) — Nắm cách mock streaming response cho AI Chat UI.
2. Đọc **[explain.md](explain.md)** (5 phút) — Nắm cách hiển thị các loại Card theo `StopCategory` (nhà hàng, chỗ chơi, tham quan...).
3. Mở **[person-5-frontend-growth.md](docs/04-tasks/person-5-frontend-growth.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` phụ trách.

---

### 🅶️ Cyber Security & DevOps (Đinh Tiến Luân)
> **Mục tiêu**: Nắm hạ tầng Docker, CI/CD GitHub Actions, Pydantic Input/Output Validation, Security Middlewares & Pentest.

1. Đọc **[security-guidelines.md](docs/05-security/security-guidelines.md)** (5 phút) — Checklist bảo mật OWASP, Pydantic sanitization, rate limit.
2. Đọc **[contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md)** (3 phút) — Quy trình review contract và dựng CI/CD từ Sprint 0.
3. Mở **[person-6-security-devops.md](docs/04-tasks/person-6-security-devops.md)** (2 phút) — Xem danh sách các mã task `TASK-xxx` phụ trách.

---

## 💻 2. Hướng Dẫn Chạy Môi Trường Dev Lần Đầu (5 Phút)

### Bước 1: Clone repo & chuẩn bị file môi trường
```bash
git clone <repo-url>
cd Group_Project
```

### Bước 2: Khởi động Backend (Python FastAPI)
```bash
cd backend
cp .env.example .env

# Khởi động PostgreSQL & Redis qua Docker
docker compose up -d

# Cài đặt dependency bằng Poetry (hoặc pip)
poetry install
poetry run alembic upgrade head

# Chạy server FastAPI dev (reload tự động)
poetry run uvicorn app.main:app --reload --port 8000
```
> Truy cập Swagger API Docs tại: `http://localhost:8000/docs`

### Bước 3: Khởi động Frontend (React + Vite)
```bash
cd ../frontend
npm install
npm run dev
```
> Truy cập Web UI tại: `http://localhost:5173`

---

## 🔄 3. Bộ Quy Trình Phối Hợp & Vận Hành Chi Tiết (Full Workflow Guide)

### 3.1. Lộ Trình Đọc Tài Liệu Quy Trình (Workflow Reading Map)

| Tình huống / Nhu cầu thực tế | File tài liệu cần đọc | Nội dung chính nắm được |
|---|---|---|
| **Bắt đầu dự án (Sprint 0)** | [contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md) | Cơ chế code song song từ ngày 1 bằng OpenAPI contract, MSW mock & schema Pydantic/SQLAlchemy |
| **Bắt đầu nhận 1 task mới** | [git-workflow.md](docs/01-workflow/git-workflow.md) & [branch-naming.md](docs/01-workflow/branch-naming.md) | Quy tắc tạo nhánh (`feature/TASK-xxx`), quy trình làm việc từ task ➜ PR ➜ Merge |
| **Khi viết commit message** | [commit-convention.md](docs/01-workflow/commit-convention.md) | Định dạng Conventional Commits chuẩn (`feat(auth): ...`, `fix(ai): ...`) |
| **Bàn giao task (Xong / Blocked / Nhảy vào làm hộ)** | [cross-team-collaboration.md](docs/01-workflow/cross-team-collaboration.md) (Phần 3) | 4 Kịch bản bàn giao công việc: Tự kiểm tra, tick done, ghi Handover Note, báo tin kênh #dev |
| **Thêm hoặc sửa tính năng giữa chừng** | [cross-team-collaboration.md](docs/01-workflow/cross-team-collaboration.md) (Phần 1) | Quy trình Contract Change (đổi API/Schema) & Feature Proposal (tính năng mới lớn) |
| **Review PR cho đồng đội (Buddy)** | [code-review-checklist.md](docs/01-workflow/code-review-checklist.md) | Checklist 10 tiêu chí kiểm tra chất lượng code, bảo mật & test coverage trước khi Approve |

---

### 3.2. Quy Trình Chọn Task & Code Theo Task (Task Execution)
1. **Tra cứu Task**: Mỗi thành viên mở file task cá nhân (`docs/04-tasks/person-x-*.md`) hoặc bảng tổng `docs/TASKS.md`.
2. **Tạo nhánh (Branch)**: Tạo nhánh theo cú pháp chuẩn: `git checkout -b feature/TASK-xxx-mo-ta-ngan` (xem [branch-naming.md](docs/01-workflow/branch-naming.md)).
3. **Thực thi code**: Chỉ chỉnh sửa các file thuộc `Target Files` và đảm bảo hoàn thành 100% `Acceptance Criteria` của task.
4. **Viết Commit Message**: Tuân thủ Conventional Commits chuẩn: `feat(scope): mô tả` hoặc `fix(scope): mô tả` (xem [commit-convention.md](docs/01-workflow/commit-convention.md)).

---

### 3.3. Quy Trình Báo Cáo Tiến Độ Hàng Ngày (Daily Progress Reporting)
1. **Daily Update Async (Gửi trước 9h00 sáng trên kênh team)**:
   - 🟢 **Hôm qua**: Đã hoàn thành `TASK-xxx` (kèm PR link nếu có).
   - 🟡 **Hôm nay**: Sẽ làm `TASK-yyy`.
   - 🔴 **Blocker**: Vấn đề bị nghẽn (nếu có).
2. **Cập nhật Task Board**: Đổi icon trạng thái trong file task cá nhân và `docs/04-tasks/task-board.md`:
   - `🔲 To Do` ➔ `🟡 In Progress` ➔ `🔵 In Review` ➔ `✅ Done` (hoặc `🔴 Blocked`).

---

### 3.4. Quy Trình Bàn Giao Công Việc (Task Handover — 4 Kịch Bản Chi Tiết)

#### 🟢 Kịch bản 1: Bàn giao khi HOÀN THÀNH Task (Task Completion)
1. **Tự kiểm tra (Self-Check)**: Chạy test local pass clean (`pytest backend`, `npm run test`, `ruff check`).
2. **Tick Done**: Đổi `[ ]` thành `[x]` trong file task cá nhân và `docs/TASKS.md`.
3. **Mở Pull Request**: Mở PR dựa trên template [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md), tag **Buddy / Reviewer**.
4. **Báo tin bàn giao**: Nhắn kênh `#dev`:
   ```
   ✅ [DONE] TASK-102: User Registration & Password Hashing
   PR: #12 (https://github.com/.../pull/12)
   Reviewer: @BE-Platform (Buddy)
   ```

#### 🔄 Kịch bản 2: Bàn giao khi NHỜ LÀM HỘ / CHUYỂN GIAO DỞ DANG (Cross-Person Handover)
1. **Push trạng thái dở dang**: Push code lên branch `feature/TASK-xxx-wip`.
2. **Viết Handover Note** trên PR/Issue:
   ```markdown
   ### 🔄 Ghi chú Bàn giao Task: TASK-304
   - **Người bàn giao**: @Tạ Quang Huy ➔ **Người nhận**: @Hà Đăng Huy
   - **Đã xong**: [x] Model `PlanVote`, [x] Endpoint POST `/votes`
   - **Cần làm tiếp**: [ ] Constraint unique `(plan_id, user_id)`, [ ] Aggregation response
   - **Lưu ý**: Role `VIEWER` không được vote.
   ```
3. **Đổi Assignee & Báo tin**: Đổi Assignee trên GitHub, báo kênh `#dev`.

#### 🔴 Kịch bản 3: Bàn giao khi BỊ BLOCKED > 2 tiếng (Blocked Task)
1. **Cập nhật trạng thái**: Đổi icon thành `🔴 Blocked` trên board.
2. **Báo tin chi tiết**: Nhắn trên kênh `#contract-changes` kèm tag người phụ trách:
   ```
   🔴 [BLOCKED] TASK-209: Location Agent Implementation
   Đang chờ: API GET /places/search filter category từ @Hà Đăng Huy (TASK-205)
   Tag: @Hà Đăng Huy @Đinh Tiến Luân
   ```
3. **Chuyển tạm task khác**: Nhặt 1 task độc lập khác trong backlog làm tạm trong lúc chờ gỡ block.

#### 🚀 Kịch bản 4: Bàn giao mốc cuối Sprint (Integration Day Handover)
1. **Chuyển Mock ➔ Thật**: Frontend tắt MSW (`VITE_USE_MOCK=false`), AI Agent trỏ sang PostgreSQL thật.
2. **Chạy Sanity Check E2E**: Test các luồng chính đi qua thành công.
3. **Demo 15 phút**: Mỗi thành viên demo 2-3 phút phần mình phụ trách trước toàn team.
4. **Security Sign-off**: DevOps & Security (@Đinh Tiến Luân) quét bảo mật lần cuối trước khi merge Sprint vào `main`.

---

### 3.5. Quy Trình Thêm & Sửa Tính Năng Giữa Chừng (Feature Change Management)

| Loại thay đổi | Định nghĩa | Quy trình xử lý |
|---|---|---|
| **🟢 Nhỏ (trong module cá nhân)** | Không ảnh hưởng ai khác (VD: thêm nút sắp xếp UI) | Tự code, mở PR bình thường |
| **🟡 Trung bình (Contract Change)** | Thay đổi REST API endpoint, DB Schema hoặc DTO | **Quy trình Contract Change**: Báo kênh `#contract-changes` ➜ Mở 1 PR riêng chỉ chứa thay đổi Docs (Schema/API Guide) ➜ Review chốt contract ➜ Các bên cập nhật code & mock |
| **🔴 Lớn (Feature Proposal)** | Tính năng hoàn toàn mới ngoài scope ban đầu | **Quy trình Feature Proposal**: Mở Issue với template Feature Proposal ➜ Thảo luận trong họp Weekly Sync ➜ Vote thông qua ➜ Phân công task ➜ Code |

---

### 3.6. Quy Trình Viết Tài Liệu & Tiêu Chuẩn "Docs as Code"
1. **Nguyên tắc Docs as Code**: Toàn bộ tài liệu kỹ thuật nằm trong thư mục `/docs`, được review qua PR giống hệt source code.
2. **Bắt buộc cập nhật Docs đi kèm Code**: Mọi PR có sửa đổi DB Schema, API endpoint hoặc Architecture **bắt buộc** phải sửa file doc tương ứng trong cùng PR (PR thiếu doc sẽ bị reject).
3. **Chuẩn Comment Code**:
   - Dùng JSDoc (Frontend) / Docstring PEP257 (Python Backend & AI Agent) cho hàm public.
   - Giải thích **"TẠI SAO"** khi logic phức tạp, không comment những gì code đã tự hiển thị rõ.
   - Mọi Prompt Template của AI Agent phải ghi rõ: mục đích, input mong đợi, output schema và model đang dùng.

---

### 3.7. Hướng Dẫn Thao Tác Git Từ A-Z (Pull, Branch, Commit, Push, PR, Rebase, Merge)

#### 1️⃣ Cập nhật code mới nhất từ `main` trước khi tạo branch
```bash
# Chuyển về nhánh main
git checkout main

# Tải code mới nhất từ GitHub về máy local
git pull origin main
```

#### 2️⃣ Tạo và chuyển sang nhánh làm việc mới (Create Branch)
```bash
# Cú pháp: git checkout -b <type>/<mã-task>-<mô-tả-ngắn>
# Ví dụ tạo nhánh cho TASK-102:
git checkout -b feature/TASK-102-user-registration
```

#### 3️⃣ Kiểm tra file thay đổi & Đưa vào Staging (Stage Files)
```bash
# Xem danh sách các file bạn vừa sửa hoặc tạo mới
git status

# Đưa tất cả file thay đổi vào khu vực chờ commit
git add .

# Hoặc chỉ add file cụ thể:
git add backend/app/api/v1/auth.py
```

#### 4️⃣ Viết Commit theo chuẩn Conventional Commits (Commit Changes)
Cú pháp: `git commit -m "<type>(<scope>): <mô tả ngắn>"`
```bash
git commit -m "feat(auth): thêm API đăng ký người dùng bằng FastAPI và bcrypt"
```

#### 5️⃣ Đồng bộ code mới nhất (Rebase) trước khi Push (Chống Conflict)
```bash
# Lấy lịch sử mới nhất từ remote main
git fetch origin main

# Ghép commit của bạn lên trên cùng của main mới nhất
git rebase origin/main

# Nếu có CONFLICT: sửa file bị conflict -> git add . -> git rebase --continue
```

#### 6️⃣ Đẩy nhánh lên GitHub (Push Branch)
```bash
# Push nhánh mới lên GitHub
git push origin feature/TASK-102-user-registration

# Nếu trước đó lỡ rebase và git báo rejected, dùng force-with-lease (chỉ trên nhánh cá nhân):
git push --force-with-lease origin feature/TASK-102-user-registration
```

#### 7️⃣ Mở Pull Request (PR) & Review trên GitHub
1. Truy cập giao diện Repository trên GitHub.
2. Nhấn nút **"Compare & pull request"** xuất hiện trên giao diện.
3. Điền tiêu đề và nội dung PR theo template [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).
4. Gán người review tại ô **Reviewers** (chọn Buddy phụ trách cùng mảng).
5. Chọn Base branch là `main`.
6. Đợi CI GitHub Actions chạy xong (đảm bảo Lint Check & Pytest pass 100%).

#### 8️⃣ Merge PR & Dọn Dẹp Nhánh Local (Merge & Cleanup)
1. Sau khi Reviewer bấm **Approve** và CI Pass: Nhấn nút **"Squash and merge"** trên GitHub.
2. Nhấn nút **"Delete branch"** trên GitHub để xóa nhánh remote.
3. Chạy các lệnh dọn dẹp bên dưới máy local:
```bash
# Chuyển về main
git checkout main

# Tải code đã merge mới nhất từ GitHub về
git pull origin main

# Xóa nhánh cá nhân vừa hoàn thành khỏi máy local
git branch -d feature/TASK-102-user-registration
```

---

## 🚀 4. Lộ Trình 10 Bước Chi Tiết Cho Người Mới Bắt Đầu (Step-by-Step Beginner Walkthrough)

> Dành cho thành viên mới chưa từng làm dự án nhóm: Hãy làm theo chính xác 10 bước này từ ngày đầu tiên!

1. **Bước 1 — Setup máy**: Clone repo ➔ Tạo file `.env` từ `.env.example` ➔ Chạy Docker `docker compose up -d` ➔ Khởi động Backend FastAPI & Frontend React.
2. **Bước 2 — Nhận Task**: Mở file task cá nhân (`docs/04-tasks/person-x-*.md`), chọn 1 task ở trạng thái `🔲 To Do` (VD: `TASK-102`).
3. **Bước 3 — Đọc Yêu Cầu**: Đọc kĩ `Target Files` và `Acceptance Criteria` của task đó trong [`docs/TASKS.md`](docs/TASKS.md).
4. **Bước 4 — Tạo Nhánh**: Mở Terminal ➔ `git checkout main` ➔ `git pull origin main` ➔ `git checkout -b feature/TASK-102-user-registration`.
5. **Bước 5 — Code & Test Local**: Chỉnh sửa code trong đúng các file quy định. Chạy linter & test local (`pytest backend`, `npm run test`, `ruff check`).
6. **Bước 6 — Commit Code**: `git add .` ➔ `git commit -m "feat(auth): thêm API đăng ký user"`.
7. **Bước 7 — Rebase & Push**: `git fetch origin main` ➔ `git rebase origin/main` ➔ `git push origin feature/TASK-102-user-registration`.
8. **Bước 8 — Mở PR & Tick Done**: Mở PR trên GitHub ➔ Đổi ô check `[ ]` thành `[x]` trong file task ➔ Tag Buddy vào review.
9. **Bước 9 — Báo Bàn Giao**: Nhắn tin trên kênh `#dev` báo PR đã sẵn sàng review.
10. **Bước 10 — Merge & Clean**: Khi PR được Approve và CI Pass ➔ Bấm **Squash and merge** ➔ Chạy `git checkout main` & `git pull origin main`.

---

## ❓ 5. Các Câu Hỏi Thường Gặp & Cách Sửa Lỗi (FAQ & Troubleshooting)

### 🔴 FAQ 1: Lỡ commit nhầm file bí mật (API Key / `.env` / Password)?
- **Cách xử lý**:
  1. Xóa ngay API Key / Secret đó khỏi file.
  2. Chạy lệnh hủy theo dõi file: `git rm --cached .env`
  3. Kiểm tra file `.gitignore` đã có dòng `.env` chưa.
  4. Commit lại: `git commit -m "fix(security): xóa file .env khỏi git tracking"`.

### 🔴 FAQ 2: Khi chạy `git rebase origin/main` bị báo CONFLICT?
- **Cách xử lý**:
  1. Gõ `git status` để xem các file bị conflict.
  2. Mở file đó trong VS Code, tìm các đoạn có ký tự `<<<<<<< HEAD` và `>>>>>>>`.
  3. Giữ lại đoạn code đúng, xóa các ký tự đánh dấu conflict đi và lưu file lại.
  4. Gõ: `git add .`
  5. Gõ: `git rebase --continue` (tuyệt đối KHÔNG gõ `git commit` lúc này).

### 🔴 FAQ 3: Môi trường dev (Backend/Frontend) bị lỗi sau khi pull code mới về?
- **Cách xử lý**:
  - **Backend**: 
    1. Cập nhật thư viện: `cd backend && poetry install`
    2. Restart Docker: `docker compose restart`
    3. Chạy migration mới: `poetry run alembic upgrade head`
  - **Frontend**:
    1. Cập nhật package: `cd frontend && npm install`
    2. Restart dev server: `npm run dev`

---

## ⚡ Cheatsheet Tóm Tắt Quy Trình 6 Bước Hàng Ngày

```
1. Chọn Task      → Đọc docs/TASKS.md hoặc file task cá nhân (person-x-*.md)
2. Tạo Branch     → git checkout -b feature/TASK-102-mo-ta-ngan
3. Code & Test    → Code theo đúng Target Files & Acceptance Criteria. Run test passing.
4. Tick Done      → Đổi [ ] thành [x] trên file task cá nhân & docs/TASKS.md
5. Mở PR          → Push code, mở PR theo template .github/PULL_REQUEST_TEMPLATE.md, tag Reviewer / Buddy
6. Bàn giao       → Báo tin trên kênh #dev theo đúng quy trình bàn giao (cross-team-collaboration.md)
```

---

## 🗺️ 6. Bản Đồ Cây Tài Liệu (Sitemap Nhanh)

```
Group_Project/
├── README.md                          ← Điểm bắt đầu chính của Repository
├── guides.md                          ← BẠN ĐANG Ở ĐÂY (Hướng dẫn nhập môn & lộ trình đọc)
├── feature.md                         ← Danh sách 42 tính năng chuẩn hóa
├── explain.md                         ← Giải thích luồng vận hành chi tiết + DeepSeek API
├── CONTRIBUTING.md                    ← Quy định đóng góp code & tóm tắt bàn giao
├── .env.example                       ← Mẫu biến môi trường chuẩn
│
├── docs/
│   ├── TASKS.md                       ← 📌 BẢNG PHÂN RÃ MICRO-TASKS CHI TIẾT (TASK-001 -> TASK-414)
│   │
│   ├── 00-overview/                   ← Tổng quan dự án & nhân sự
│   │   ├── project-overview.md        ← Mục tiêu, scope MVP
│   │   ├── tech-stack.md              ← Công nghệ chi tiết (FastAPI, React, LangGraph)
│   │   └── team-roles.md              ← Phân vai trò 6 thành viên & Ma trận RACI
│   │
│   ├── 01-workflow/                   ← Quy trình phối hợp team
│   │   ├── contract-first-workflow.md ← Quy trình làm song song từ ngày 1
│   │   ├── cross-team-collaboration.md← Thay đổi giữa chừng, giúp đỡ & BÀN GIAO CÔNG VIỆC
│   │   ├── git-workflow.md            ← Quy tắc branch, PR, merge
│   │   ├── branch-naming.md           ← Đặt tên branch
│   │   ├── commit-convention.md       ← Chuẩn commit message
│   │   └── code-review-checklist.md   ← Checklist review PR
│   │
│   ├── 02-standards/                  ← Tiêu chuẩn kỹ thuật
│   │   ├── coding-conventions.md      ← Python PEP8, FastAPI, Pydantic, React style
│   │   ├── naming-conventions.md      ← Quy tắc đặt tên biến/hàm/file
│   │   ├── api-design-guide.md        ← Chuẩn REST API endpoint & response format
│   │   ├── documentation-guide.md     ← Quy tắc viết tài liệu
│   │   └── testing-guide.md           ← Chuẩn viết Pytest & Vitest
│   │
│   ├── 03-architecture/               ← Kiến trúc kỹ thuật
│   │   ├── system-architecture.md     ← Sơ đồ tổng thể hệ thống
│   │   ├── database-schema.md         ← SQLAlchemy/Prisma DB Models & Indexes
│   │   └── ai-agent-architecture.md   ← LangGraph Python Multi-Agent Architecture
│   │
│   ├── 04-tasks/                      ← Task cá nhân theo 6 thành viên
│   │   ├── task-board.md              ← Bảng theo dõi tiến độ tổng 6 track
│   │   ├── person-1-backend-core.md   ← Tạ Quang Huy (Backend Core & AI Integration)
│   │   ├── person-2-backend-platform.md ← Hà Đăng Huy & Phạm Đình Ánh Dương (Backend Platform & Services)
│   │   ├── person-3-ai-engineer.md    ← Nguyễn Tùng Dương & Tạ Quang Huy (AI Agent Team)
│   │   ├── person-4-frontend-core.md  ← Hà Đăng Huy (Frontend Core UI)
│   │   ├── person-5-frontend-growth.md← Nguyễn Minh Đức (Frontend AI & Growth UI)
│   │   └── person-6-security-devops.md← Đinh Tiến Luân (Cyber Security & DevOps)
│   │
│   ├── 05-security/                   ← Bảo mật
│   │   └── security-guidelines.md     ← Standard security checklist & Pydantic sanitization
│   │
│   └── 06-design/                     ← UI/UX Design (Sprint 0)
│       ├── README.md                  ← Overview + quy trình Design → Code
│       ├── design-tokens.md           ← Palette, typography, spacing (TASK-009)
│       ├── user-flows.md              ← Flowchart các luồng chính (TASK-010)
│       ├── wireframes/                ← Wireframe từng page (TASK-010)
│       └── mockups.md                 ← Hi-fi mockups trên Figma (TASK-011)
```
