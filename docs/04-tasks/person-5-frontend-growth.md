# 👤 Person 5 — Frontend Dev B (AI Experience & Growth)

> **Sở hữu**: UI Chat AI, Landing page, i18n, chia chi phí, Admin Dashboard UI.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 1 Task | 0/1 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | 0/2 | 🔲 To Do |
| **Sprint 2** | 0 Tasks (Support AI Chat Mock) | 0/0 | 🔲 To Do |
| **Sprint 3** | 0 Tasks (Support PDF Preview) | 0/0 | 🔲 To Do |
| **Sprint 4** | 5 Tasks | 0/5 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — MSW Streaming Mock Setup
- [ ] **`TASK-005`** **MSW Streaming Mock Setup for AI Chat**
  - **Feature**: #31, #32
  - **Target Files**: `frontend/src/mocks/handlers/ai.ts`
  - **Acceptance Criteria**: Simulates SSE / WebSocket chunked responses for chat UI testing without calling real backend.

### Sprint 1 — Landing Page & i18n
- [ ] **`TASK-114`** **Landing Page & Hero Section**
  - **Feature**: #39
  - **Target Files**: `frontend/src/features/landing/pages/LandingPage.tsx`
  - **Acceptance Criteria**: Showcases 6 event types (Travel, Dining, Hangout, Entertainment, Sightseeing, Custom) with CTA buttons.
- [ ] **`TASK-115`** **i18n Setup (react-i18next)**
  - **Feature**: #40
  - **Target Files**: `frontend/src/i18n/`, `frontend/src/locales/` (`vi.json`, `en.json`)
  - **Acceptance Criteria**: Header language toggle switches entire UI seamlessly between Vietnamese and English.

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
- [ ] **`TASK-409`** **Shared Expense Calculator UI**
  - **Feature**: #41
  - **Target Files**: `frontend/src/features/expense/pages/ExpensePage.tsx`
  - **Acceptance Criteria**: Displays total cost, per-person debt matrix, settled status toggle.
- [ ] **`TASK-410`** **Admin Dashboard UI Screen**
  - **Feature**: #36, #37
  - **Target Files**: `frontend/src/features/admin/pages/AdminDashboardPage.tsx`
  - **Acceptance Criteria**: Renders token cost charts (Recharts), active user stats, API usage breakdown, user table.

---

## 🤝 Handover & Review Guidelines (Person 5)

1. **Buddy / Backup**: `Person 4` (Frontend Dev A)
2. **Task Completion**: Run `npm run lint` and `npm run test`. Push branch `feature/TASK-xxx` and tag `@FE-A` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
