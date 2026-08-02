# Thêm Tính Năng Giữa Chừng & Nhảy Vào Code Của Nhau Không Conflict

> Tài liệu này giải quyết 2 vấn đề thực tế khi team 6 người làm việc song song:
> 1. Muốn thêm/sửa tính năng khi dự án đang chạy → làm thế nào?
> 2. Muốn 1 người nhảy vào giúp phần của người khác → tổ chức code/task ra sao?

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
   Person A sửa dòng 50-80 của EventService.ts
   Person B sửa dòng 60-90 của EventService.ts
   → CONFLICT khi merge

✅ ĐÚNG: mỗi người sửa file/module riêng, giao tiếp qua interface
   Person A code PlanService.ts (tạo plan)
   Person B code VoteService.ts (tạo vote)
   Cả 2 chỉ import interface, không sửa chung 1 file
   → KHÔNG CONFLICT
```

### 2.2. Cấu trúc code theo Module — chìa khóa chống conflict

NestJS đã hỗ trợ module hóa sẵn. Tổ chức thư mục theo **domain module**, mỗi module là lãnh thổ của 1-2 người:

```
backend/src/
├── auth/                    ← Person 1 sở hữu
│   ├── auth.module.ts
│   ├── auth.service.ts      ← Logic đăng nhập/đăng ký
│   ├── auth.controller.ts   ← Endpoint /auth/*
│   ├── guards/              ← AuthGuard, RolesGuard
│   └── dto/                 ← LoginDto, RegisterDto
│
├── event/                   ← Person 1 sở hữu, Person 2 có thể đóng góp
│   ├── event.module.ts
│   ├── event.service.ts     ← Logic CRUD event
│   ├── event.controller.ts
│   ├── plan/                ← Sub-module cho Plan
│   │   ├── plan.service.ts
│   │   └── plan.controller.ts
│   └── vote/                ← Sub-module cho Vote
│       ├── vote.service.ts
│       └── vote.controller.ts
│
├── places/                  ← Person 2 sở hữu
│   ├── places.module.ts
│   ├── places.service.ts    ← Gọi Google Places API + cache
│   └── places.controller.ts
│
├── ai/                      ← Person 3 (AI Engineer) sở hữu
│   ├── ai.module.ts
│   ├── orchestrator/
│   │   └── orchestrator.service.ts
│   ├── agents/
│   │   ├── location.agent.ts    ← Mỗi agent 1 file riêng
│   │   ├── plan.agent.ts
│   │   ├── research.agent.ts
│   │   ├── conflict.agent.ts
│   │   └── ...
│   └── ai.controller.ts
│
└── notification/            ← Person 2 sở hữu
    ├── notification.module.ts
    ├── notification.service.ts
    └── email.service.ts
```

**Quy tắc vàng**: Mỗi module expose ra **Service interface** (public methods). Người khác muốn dùng → `import { PlanService } from '../event/plan/plan.service'`, gọi method công khai. **Không bao giờ sửa code bên trong module của người khác** mà không báo trước.

### 2.3. Cách chia task để người khác nhảy vào giúp được

**Nguyên tắc: Chia nhỏ theo chiều dọc (Vertical Slice), không theo chiều ngang.**

```
❌ CHIỀU NGANG (khó nhảy vào giúp):
   Task: "Làm toàn bộ module Event"
   → Quá to, chỉ 1 người hiểu, người khác không biết bắt đầu từ đâu

✅ CHIỀU DỌC (dễ nhảy vào giúp):
   Task 1: "API tạo event mới (POST /events)" — 1 endpoint, 1 service method, 1 test
   Task 2: "API mời thành viên (POST /events/:id/invite)" — 1 endpoint riêng
   Task 3: "API lấy danh sách member (GET /events/:id/members)" — 1 endpoint riêng
   → Mỗi task độc lập, ai rảnh nhặt task nào cũng được
```

**Mỗi task (Issue) nên có đủ 4 phần:**
```markdown
## Task: API tạo event mới

### Input (request)
POST /api/v1/events
Body: { name: string, type: EventType, startDate: string, endDate: string }

### Output (response)
201: { success: true, data: { id: string, name: string, ... } }
400: { success: false, error: { code: "VALIDATION_ERROR", ... } }

### Acceptance Criteria
- [ ] Chỉ user đã đăng nhập mới tạo được (AuthGuard)
- [ ] Người tạo tự động thành Owner trong EventMember
- [ ] Validate: name không rỗng, startDate < endDate
- [ ] Test: happy path + validation fail + unauthorized

### File cần tạo/sửa
- `event/event.service.ts` → method `createEvent()`
- `event/event.controller.ts` → handler `POST /events`
- `event/dto/create-event.dto.ts` → Zod/class-validator schema
- `event/event.service.spec.ts` → unit test
```

> Với format này, **bất kỳ ai** đọc xong đều biết: cần code gì, ở file nào, kết quả đúng trông ra sao. Không cần hỏi lại người phụ trách.

### 2.4. Quy trình nhảy vào giúp người khác

Khi Person B muốn giúp Person A (VD: BE Dev B giúp BE Dev A làm Vote module vì A đang bị quá tải):

```
1. Nhặt task     → Vào board, chọn task chưa ai làm trong module của A
2. Báo trước     → Message kênh #dev: "Mình nhặt task Vote API nhé @A"
3. Đọc context   → Đọc file task của A (person-1-backend-core.md) + schema liên quan
4. Code đúng chỗ → Code trong đúng thư mục module, theo đúng convention
5. PR tag owner  → Mở PR, tag A làm reviewer (A hiểu context nhất)
6. A review      → A approve hoặc góp ý → merge
```

**Điều kiện để nhảy vào mượt:**
- Task đã được chia nhỏ kiểu vertical slice (mục 2.3)
- Task có Acceptance Criteria rõ ràng
- Code theo convention chung (xem [coding-conventions.md](../02-standards/coding-conventions.md))
- Chủ module review PR → đảm bảo code mới khớp với kiến trúc module

### 2.5. Buddy System — mỗi người có 1 backup

Để bất kỳ ai cũng có thể nhảy vào giúp bất kỳ ai, team nên áp dụng **Buddy System**:

| Người | Buddy (backup) | Lý do |
|---|---|---|
| BE Dev A (Core) | BE Dev B (Platform) | Cùng backend, hiểu NestJS/Prisma |
| BE Dev B (Platform) | BE Dev A (Core) | Ngược lại |
| AI Engineer | BE Dev A (Core) | AI cần hiểu schema, BE-A hiểu schema rõ nhất |
| FE Dev A (Core) | FE Dev B (Growth) | Cùng frontend, cùng React |
| FE Dev B (Growth) | FE Dev A (Core) | Ngược lại |
| Security/DevOps | Ai cũng được | Review PR cross-team là việc thường ngày |

**Buddy làm gì:**
- Review **mọi PR** của người mình backup → luôn hiểu code của họ
- Khi buddy bận/nghỉ → nhặt task thay, không bị tắc tiến độ
- Weekly: dành 15 phút sync nhanh những thay đổi kiến trúc trong module

### 2.6. Tránh conflict Git — mẹo thực tế

| Mẹo | Chi tiết |
|---|---|
| **1 PR ≤ 400 dòng diff** | PR càng nhỏ, càng ít chance conflict với PR khác |
| **Rebase thường xuyên** | Mỗi sáng: `git fetch origin && git rebase origin/develop` trước khi code tiếp |
| **Không sửa file dùng chung** nếu không cần | File như `app.module.ts`, `prisma/schema.prisma` — chỉ sửa khi thật sự cần, và merge nhanh |
| **Tách file thay vì nhét chung** | Nếu 2 người cùng cần thêm route → tách thành 2 file module riêng, import vào `app.module.ts` 1 dòng thay vì sửa chung 1 file routes lớn |
| **Lock file (package-lock.json)** | Nếu conflict ở lock file → xóa lock, chạy `npm install` lại, commit lock mới |
| **Schema Prisma** | Người sở hữu schema (BE Dev A) nên merge PR đổi schema **trước**, rồi mọi người rebase lên. Không để 2 PR đổi schema cùng lúc |

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
1. Nhặt task nhỏ (vertical slice) từ board
2. Báo người phụ trách trên kênh #dev
3. Đọc file task + schema liên quan
4. Code trong đúng module, đúng convention
5. PR tag chủ module làm reviewer
```
