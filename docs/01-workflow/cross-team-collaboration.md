# Thêm Tính Năng Giữa Chừng & Nhảy Vào Code Của Nhau Không Conflict

> Tài liệu này giải quyết 3 vấn đề thực tế khi team 6 người làm việc song song:
> 1. Muốn thêm/sửa tính năng khi dự án đang chạy → làm thế nào?
> 2. Muốn 1 người nhảy vào giúp phần của người khác → tổ chức code/task ra sao?
> 3. Quy trình bàn giao công việc (Handover) khi xong task, khi bị block, hoặc khi chuyển giao task cho nhau.

---

## Phần 1: Quy Trình Thêm / Sửa Tính Năng Giữa Chừng

### 1.1. Phân loại thay đổi — xử lý khác nhau

| Loại thay đổi | Ví dụ | Ảnh hưởng | Cách xử lý |
|---|---|---|---|
| **🟢 Nhỏ — trong phạm vi 1 người** | Thêm nút "Sắp xếp theo giá" trong UI Plan | Không ai khác bị ảnh hưởng | Tự làm luôn, mở PR bình thường |
| **🟡 Trung bình — cần đổi API/response** | Thêm field `cuisine` vào endpoint `/places/search` | Frontend + AI Agent đang dùng response cũ | Quy trình **Contract Change** (mục 1.2) |
| **🔴 Lớn — tính năng mới hoàn toàn** | Thêm tính năng "Chia bill theo món" | Cần schema DB mới, API mới, UI mới | Quy trình **Feature Proposal** (mục 1.3) |

### 1.2. Contract Change (thay đổi trung bình — đổi API/schema)

Đây là quy trình đã có ở [contract-first-workflow.md](contract-first-workflow.md) mục 5, nhưng tóm tắt lại rõ hơn:

```
Phát hiện cần đổi → Báo #contract-changes → PR cập nhật docs → Người bị ảnh hưởng cập nhật code
```

**Bước chi tiết:**
1. **Báo ngay** trên kênh `#contract-changes` (Slack/Discord/Zalo):
   ```
   ⚠️ Contract Change
   Đổi gì: Thêm field `cuisine: string` vào response GET /places/search
   Lý do: AI Agent cần filter theo loại đồ ăn cho DINING event
   Ảnh hưởng: @FE-A (đang render list places), @AI-Engineer (Location Agent)
   PR docs: #45
   ```
2. **Mở 1 PR riêng** chỉ chứa thay đổi docs (schema, API guide, shared-types) — review nhanh trong ngày, không để tồn đọng.
3. **Ưu tiên backward-compatible**: thêm field mới (optional) thay vì đổi/xóa field cũ → người khác không bị break ngay.
4. Người bị ảnh hưởng cập nhật code/mock của mình theo contract mới.

### 1.3. Feature Proposal (tính năng mới lớn)

Khi ai đó muốn thêm một tính năng hoàn toàn mới (không có trong backlog ban đầu):

**Bước 1: Mở Issue "Feature Proposal"** với template:
```markdown
## 🆕 Feature Proposal: [Tên tính năng]

### Mô tả ngắn
[1-2 câu: tính năng này làm gì, giải quyết vấn đề gì]

### User story
Là [ai], tôi muốn [làm gì], để [đạt được gì].

### Ảnh hưởng kỹ thuật
- [ ] Cần thêm/đổi DB schema? → Ghi rõ bảng/field nào
- [ ] Cần thêm/đổi API endpoint? → Ghi rõ endpoint nào
- [ ] Cần thêm UI mới? → Mô tả sơ bộ màn hình
- [ ] Ảnh hưởng AI Agent? → Agent nào cần đổi
- [ ] Ước lượng thời gian: [x ngày công]

### Ai cần tham gia
@backend-a @frontend-b ...

### Ưu tiên
- [ ] Phải có cho MVP (chặn demo)
- [ ] Nên có (nâng điểm)
- [ ] Nice-to-have (làm nếu còn thời gian)
```

**Bước 2: Thảo luận trong weekly sync** (hoặc async trên Issue nếu gấp):
- Cả team vote: có làm không? Ưu tiên nào? Sprint nào?
- Nếu đồng ý → phân công người làm, tạo sub-task.

**Bước 3: Nếu cần đổi contract** → chạy quy trình Contract Change (1.2) trước khi code.

**Bước 4: Code theo quy trình PR bình thường**, link PR về Issue Feature Proposal.

### 1.4. Nguyên tắc vàng khi thay đổi giữa chừng

| Nguyên tắc | Giải thích |
|---|---|
| **Thêm, đừng sửa** | Thêm field mới thay vì đổi field cũ. Thêm endpoint mới thay vì đổi response endpoint cũ. Backward-compatible = không ai bị break. |
| **Báo trước, đừng báo sau** | Đổi xong rồi mới nói → người khác code cả ngày trên contract cũ, phí công. Báo trước → người ta chuẩn bị. |
| **1 PR = 1 việc** | Đừng nhét tính năng mới vào PR đang fix bug. Tách riêng để dễ review, dễ revert nếu có lỗi. |
| **Feature flag nếu chưa xong** | Code xong 50% nhưng muốn merge sớm? Dùng feature flag (`if (FEATURE_X_ENABLED)`) để merge vào main mà không ảnh hưởng người khác. |

---

## Phần 2: Chia Task Để Nhảy Vào Code Của Nhau Không Conflict

### 2.1. Tại sao dễ bị conflict?

```
❌ SAI: 2 người cùng sửa 1 file lớn
   Person A sửa dòng 50-80 của EventService.py
   Person B sửa dòng 60-90 của EventService.py
   → CONFLICT khi merge

✅ ĐÚNG: mỗi người sửa file/module riêng, giao tiếp qua interface
   Person A code plan_service.py (tạo plan)
   Person B code vote_service.py (tạo vote)
   Cả 2 chỉ import interface, không sửa chung 1 file
   → KHÔNG CONFLICT
```

### 2.2. Cấu trúc code theo Module — chìa khóa chống conflict

FastAPI hỗ trợ APIRouter & Services rõ ràng. Tổ chức thư mục theo **domain module**, mỗi module là lãnh thổ của 1-2 người:

```
backend/app/
├── core/                    ← Config, security, DB engine
├── models/                  ← SQLAlchemy DB Models
├── schemas/                 ← Pydantic v2 DTOs
├── api/v1/                  ← FastAPI APIRouters
│   ├── auth.py              ← Person 1 sở hữu
│   ├── events.py            ← Person 1 sở hữu
│   ├── plans.py             ← Person 1 sở hữu
│   ├── votes.py             ← Person 1 sở hữu
│   ├── places.py            ← Person 2 sở hữu
│   ├── utils.py             ← Person 2 sở hữu
│   ├── export.py            ← Person 2 sở hữu
│   └── ai.py                ← Person 3 sở hữu
├── services/                ← Service layer (auth_service, event_service, places_service...)
└── ai_agents/               ← Person 3 (AI Engineer) sở hữu
    ├── orchestrator.py
    └── agents/
        ├── location_agent.py
        ├── plan_agent.py
        └── ...
```

**Quy tắc vàng**: Mỗi module expose ra **Service class / function** (public methods). Người khác muốn dùng → `from app.services.plan_service import plan_service`, gọi method công khai. **Không bao giờ sửa code bên trong module của người khác** mà không báo trước.

### 2.3. Cách chia task để người khác nhảy vào giúp được

**Nguyên tắc: Chia nhỏ theo chiều dọc (Vertical Slice), không theo chiều ngang.**

```
❌ CHIỀU NGANG (khó nhảy vào giúp):
   Task: "Làm toàn bộ module Event"
   → Quá to, chỉ 1 người hiểu, người khác không biết bắt đầu từ đâu

✅ CHIỀU DỌC (dễ nhảy vào giúp):
   Task 1: "API tạo event mới (POST /events)" — 1 endpoint, 1 service method, 1 test
   Task 2: "API mời thành viên (POST /events/:id/invitations)" — 1 endpoint riêng
   Task 3: "API lấy danh sách member (GET /events/:id/members)" — 1 endpoint riêng
   → Mỗi task độc lập, ai rảnh nhặt task nào cũng được (theo đúng mã TASK-xxx trong docs/TASKS.md)
```

### 2.4. Quy trình nhảy vào giúp người khác

Khi Person B muốn giúp Person A (VD: BE Dev B giúp BE Dev A làm Vote module vì A đang bị quá tải):

```
1. Nhặt task     → Vào board/TASKS.md, chọn task chưa ai làm trong module của A (VD: TASK-304)
2. Báo trước     → Message kênh #dev: "Mình nhặt TASK-304 Vote API nhé @A"
3. Đọc context   → Đọc file TASKS.md & file task của A (person-1-backend-core.md)
4. Code đúng chỗ → Code trong đúng thư mục module, theo đúng convention Pydantic/SQLAlchemy
5. PR tag owner  → Mở PR, tag A làm reviewer (A hiểu context nhất)
6. A review      → A approve hoặc góp ý → merge
```

### 2.5. Buddy System — mỗi người có 1 backup

| Người | Buddy (backup) | Lý do |
|---|---|---|
| BE Dev A (Core) | BE Dev B (Platform) | Cùng backend Python FastAPI, hiểu SQLAlchemy |
| BE Dev B (Platform) | BE Dev A (Core) | Ngược lại |
| AI Engineer | BE Dev A (Core) | AI cần hiểu schema, BE-A hiểu schema rõ nhất |
| FE Dev A (Core) | FE Dev B (Growth) | Cùng frontend, cùng React |
| FE Dev B (Growth) | FE Dev A (Core) | Ngược lại |
| Security/DevOps | Ai cũng được | Review PR cross-team là việc thường ngày |

---

## Phần 3: Quy Trình Bàn Giao Công Việc (Task Handover Workflow)

Để việc theo dõi tiến độ công việc giữa các thành viên diễn ra minh bạch, rõ ràng, dự án quy định 4 kịch bản bàn giao công việc cụ thể:

### 3.1. Bàn Giao Khi Hoàn Thành Task (Task Completion Handover)

Khi hoàn thành một micro-task (Ví dụ: `TASK-102`):

1. **Tự kiểm tra (Self-Check)**:
   - Chạy linter & test local pass clean: `ruff check backend` và `pytest backend` (hoặc `npm run test` phía FE).
   - Kiểm tra code đáp ứng đủ các tiêu chí trong **Acceptance Criteria** của task trong `docs/TASKS.md`.
2. **Cập nhật trạng thái Task**:
   - Mở file task cá nhân (`person-x-*.md`) và file `docs/TASKS.md`, đổi ô tick từ `[ ]` thành `[x]`.
3. **Mở Pull Request & Tag Reviewer**:
   - Đặt tên branch: `feature/TASK-102-user-registration`.
   - Mở PR dựa trên template `.github/PULL_REQUEST_TEMPLATE.md`.
   - Tag **Buddy / Chủ module** làm reviewer.
4. **Báo tin bàn giao trên kênh `#dev`**:
   ```
   ✅ [DONE] TASK-102: User Registration & Password Hashing
   PR: #12 (https://github.com/.../pull/12)
   Reviewer: @BE-B (Buddy)
   ```

---

### 3.2. Bàn Giao Khi Nhờ Người Khác Làm Hộ / Nhảy Vào Giúp (Cross-Person Handover)

Khi Person A chuyển giao task đang dở cho Person B (hoặc Person B nhảy vào giúp):

1. **Push trạng thái code hiện tại**:
   - Push toàn bộ code lên branch `feature/TASK-xxx-wip` (kể cả chưa xong hoàn toàn).
   - Đảm bảo không để code dở dang trên máy cá nhân mà người khác không truy cập được.
2. **Để lại Ghi chú Bàn giao (Handover Note)** trên Issue/PR dở:
   ```markdown
   ### 🔄 Ghi chú Bàn giao Task: TASK-304
   - **Người bàn giao**: @BE-A → **Người nhận**: @BE-B
   - **Đã làm xong**:
     - [x] Tạo SQLAlchemy Model `PlanVote`
     - [x] Endpoint `POST /events/:id/plans/:planId/votes` nhận vote UP/DOWN
   - **Còn lại cần làm tiếp**:
     - [ ] Kiểm tra constraint unique `(plan_id, user_id)`
     - [ ] Tổng hợp kết quả vote trả về cho FE
   - **Lưu ý kỹ thuật**: Cần chú ý role `VIEWER` không được vote.
   ```
3. **Chuyển Assignee**:
   - Đổi Assignee trên GitHub Projects sang Person B.
   - Báo tin trên kênh `#dev`: `🔄 [HANDOVER] TASK-304 đã chuyển giao cho @BE-B tiếp quản. Branch: feature/TASK-304-wip`.

---

### 3.3. Bàn Giao Khi Bị Block / Tắc Tiến Độ (Blocked Task Handover)

Khi một task bị block quá 2 tiếng (ví dụ: chờ API spec từ BE, chờ UI design từ FE, v.v.):

1. **Cập nhật trạng thái Blocked**:
   - Đổi trạng thái trên Task Board thành `🔴 Blocked`.
2. **Báo tin chi tiết lên kênh `#contract-changes` hoặc `#dev`**:
   ```
   🔴 [BLOCKED] TASK-209: Location Agent implementation
   Đang chờ: API GET /places/search filter theo category từ @BE-B (TASK-205)
   Ảnh hưởng: Không thể hoàn thiện agent tìm địa điểm trong Sprint 2
   Tag: @BE-B @Security
   ```
3. **Chuyển tạm sang Task khác**:
   - Trong thời gian chờ giải quyết blocker, nhặt một task độc lập khác trong backlog để không bị phí thời gian.

---

### 3.4. Bàn Giao Mốc Cuối Sprint (Integration Day Handover)

Vào ngày cuối cùng của Sprint (Integration Day):

1. **Chuyển chế độ Mock → Thật**:
   - Frontend tắt MSW mock mode (`VITE_USE_MOCK=false`), trỏ URL API về môi trường Staging/Dev server.
   - AI Engineer trỏ LangGraph Agent sang đọc/ghi DB PostgreSQL thật thay cho fixture JSON.
2. **Chạy E2E Sanity Checklist**:
   - Kiểm tra các luồng đi qua đúng Happy Path.
3. **Demo ngắn 15 phút**:
   - Mỗi người demo 2-3 phút phần mình phụ trách trước team.
4. **Sign-off**:
   - Security & DevOps quét kiểm tra bảo mật lần cuối trước khi merge nhánh Sprint vào `main`.

---

## Tóm Tắt Nhanh (Quick Reference)

### Muốn thêm tính năng mới?
```
Nhỏ (trong module mình)     → Làm luôn, PR bình thường
Trung bình (đổi API/schema) → Báo #contract-changes → PR docs → rồi code
Lớn (tính năng hoàn toàn mới) → Mở Issue Feature Proposal → weekly sync → phân công → code
```

### Muốn nhảy vào giúp người khác?
```
1. Nhặt task nhỏ (vertical slice) từ board / docs/TASKS.md
2. Báo người phụ trách trên kênh #dev
3. Đọc file TASKS.md + schema liên quan
4. Code trong đúng module, đúng convention
5. PR tag chủ module làm reviewer
```
