# 👤 Person 5 — Nguyễn Minh Đức (Frontend Dev B: AI Experience & Growth UI)

> **Người phụ trách**: **Nguyễn Minh Đức**
> **Sở hữu**: UI Realtime Chat AI streaming, Landing Page, i18n đa ngôn ngữ (VI/EN), Design Tokens & Design System, Checklist UI, Shared Expenses Calculator & Admin Dashboard UI.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 4 Tasks | 0/4 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | 0/2 | 🔲 To Do |
| **Sprint 2** | 0 Tasks (Support AI Chat Mock) | 0/0 | 🔲 To Do |
| **Sprint 3** | 1 Task (Packing Checklist UI) | 0/1 | 🔲 To Do |
| **Sprint 4** | 5 Tasks | 0/5 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — MSW Mock, User Flows & Hi-fi Mockups
- [ ] **`TASK-005`** **MSW Streaming Mock Setup for AI Chat**
  - **Feature**: #31, #32
  - **Target Files**: `frontend/src/mocks/handlers/ai.ts`
  - **Acceptance Criteria**: Simulates SSE / WebSocket chunked responses for chat UI testing without calling real backend.
- [ ] **`TASK-009`** **Design Tokens & Design System Spec**
  - **Feature**: #42
  - **Target Files**: `docs/06-design/design-tokens.md`, `frontend/src/styles/theme.ts`, `frontend/tailwind.config.js`
  - **Acceptance Criteria**: Chốt palette (light/dark), typography scale, spacing, radius, shadow; mapping sang shadcn/Tailwind theme config; là nguồn duy nhất cho mọi màn hình (feed vào TASK-111).
- [ ] **`TASK-010`** **User Flows & Page Wireframes**
  - **Feature**: #1 → #42
  - **Target Files**: `docs/06-design/user-flows.md`, `docs/06-design/wireframes/` (Mermaid/ASCII hoặc Figma)
  - **Acceptance Criteria**: Flowchart các luồng chính: register/login → tạo event → mời member → tạo/vote plan → confirm → chia chi phí; wireframe từng page chốt layout + component + empty/loading/error state.
- [ ] **`TASK-011`** **Hi-fi Mockups, Component Library & Accessibility**
  - **Feature**: #42
  - **Target Files**: `docs/06-design/mockups.md` (link Figma), `frontend/src/components/ui/` (variants)
  - **Acceptance Criteria**: Hi-fi mockups cho 6 EventType + AI chat streaming + expense/settlement; component variants (Button/Input/Card/Dialog/Toast) theo design tokens (TASK-009); responsive breakpoints (mobile/tablet/desktop) + contrast WCAG AA.

### Sprint 1 — Landing Page & i18n
- [ ] **`TASK-114`** **Landing Page & Hero Section**
  - **Feature**: #39
  - **Target Files**: `frontend/src/features/landing/pages/LandingPage.tsx`
  - **Acceptance Criteria**: Showcases 6 event types (Travel, Dining, Hangout, Entertainment, Sightseeing, Custom) with CTA buttons.
- [ ] **`TASK-115`** **i18n Setup (react-i18next)**
  - **Feature**: #40
  - **Target Files**: `frontend/src/i18n/`, `frontend/src/locales/` (`vi.json`, `en.json`)
  - **Acceptance Criteria**: Header language toggle switches entire UI seamlessly between Vietnamese and English.

### Sprint 3 — Packing Checklist UI
- [ ] **`TASK-317`** **Packing Checklist UI Screen**
  - **Feature**: #35
  - **Target Files**: `frontend/src/features/checklist/pages/ChecklistPage.tsx`
  - **Acceptance Criteria**: Interactive checklist with item check/uncheck, custom item add/delete, progress bar.

### Sprint 4 — Realtime Chat UI, Shared Expenses & Admin Dashboard
- [ ] **`TASK-406`** **AI Chat Interface with Streaming Output**
  - **Feature**: #31, #32
  - **Target Files**: `frontend/src/features/ai-chat/pages/ChatPage.tsx`
  - **Acceptance Criteria**: Chat interface renders streaming response, user typing indicator, suggestion quick-chips.
- [ ] **`TASK-407`** **Interactive Draft Plan Card Renderer**
  - **Feature**: #32
  - **Target Files**: `frontend/src/features/ai-chat/components/PlanCardPreview.tsx`
  - **Acceptance Criteria**: Renders AI proposal inside chat as structured card with "Accept as Draft" or "Modify" buttons.
- [ ] **`TASK-408`** **Category-Specific Stop Cards Rendering**
  - **Feature**: #25, #32
  - **Target Files**: `frontend/src/features/plan/components/StopCategoryCard.tsx`
  - **Acceptance Criteria**: Custom card designs: displays menu items for RESTAURANT, activity ticket prices for ENTERTAINMENT, opening hours/tips for SIGHTSEEING.
- [ ] **`TASK-409`** **Shared Expense & Settlement UI**
  - **Feature**: #41
  - **Target Files**: `frontend/src/features/expense/pages/ExpensePage.tsx`, `frontend/src/features/expense/components/ExpenseForm.tsx`, `frontend/src/features/expense/components/FundPoolCard.tsx`, `frontend/src/features/expense/components/SettlementTable.tsx`
  - **Acceptance Criteria**: UI tương ứng API TASK-415: form thêm expense chọn SplitType (EQUAL/EXACT/PERCENTAGE), hiển thị fund pool + từng member đóng bao nhiêu, danh sách expense, net balance từng người, bảng settlement tối ưu (ai trả ai bao nhiêu) kèm trạng thái settled toggle. Empty/loading/error states đầy đủ (theo wireframe TASK-010).
- [ ] **`TASK-410`** **Admin Dashboard UI Screen**
  - **Feature**: #36, #37
  - **Target Files**: `frontend/src/features/admin/pages/AdminDashboardPage.tsx`
  - **Acceptance Criteria**: Renders token cost charts (Recharts), active user stats, API usage breakdown, user table.

---

## 🤝 Handover & Review Guidelines (Person 5)

1. **Buddy / Backup**: `Person 4` (Frontend Dev A)
2. **Task Completion**: Run `npm run lint` and `npm run test`. Push branch `feature/TASK-xxx` and tag `@FE-A` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
