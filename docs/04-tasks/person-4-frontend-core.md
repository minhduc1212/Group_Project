# 👤 Person 4 — Hà Đăng Huy (Frontend Dev A: Core Flows UI)

> **Người phụ trách**: **Hà Đăng Huy**
> **Sở hữu**: UI cho Auth, Event Dashboard, EventType Selector, Plan Builder, Vote UI & Mapbox Integration (kiêm Backend Dev B: External APIs). Code song song với Backend Dev A qua mock (MSW), nối thật ở Integration Day.

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 1 Task | 0/1 | 🔲 To Do |
| **Sprint 1** | 3 Tasks | 0/3 | 🔲 To Do |
| **Sprint 2** | 4 Tasks | 0/4 | 🔲 To Do |
| **Sprint 3** | 3 Tasks | 0/3 | 🔲 To Do |
| **Sprint 4** | 0 Tasks (Support Testing & Polish) | 0/0 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — MSW Mock Setup
- [ ] **`TASK-004`** **MSW Mock Handlers Setup for Core APIs**
  - **Feature**: N/A
  - **Target Files**: `frontend/src/mocks/handlers/` (`auth.ts`, `events.ts`, `plans.ts`)
  - **Acceptance Criteria**: MSW intercepts `/api/v1/auth/*` và `/api/v1/events/*`, returning mock JSON adhering to OpenAPI contract.

### Sprint 1 — UI System & Auth Screens
- [ ] **`TASK-111`** **Project Skeleton & Design System (Tailwind + shadcn)**
  - **Feature**: #42
  - **Target Files**: `frontend/src/`, `frontend/tailwind.config.js`
  - **Acceptance Criteria**: Vite app builds cleanly with Tailwind CSS, shadcn components, responsive design.
- [ ] **`TASK-112`** **Login & Register UI Screens**
  - **Feature**: #1, #2
  - **Target Files**: `frontend/src/features/auth/pages/LoginPage.tsx`, `RegisterPage.tsx`
  - **Acceptance Criteria**: Form validation with React Hook Form + Zod, Google/Facebook login buttons, submit calls Auth API / MSW.
- [ ] **`TASK-113`** **Forgot Password & Profile Management UI**
  - **Feature**: #3, #4
  - **Target Files**: `frontend/src/features/auth/pages/ForgotPasswordPage.tsx`, `ProfilePage.tsx`
  - **Acceptance Criteria**: Profile page allows avatar upload and name edit, updates Zustand auth store.

### Sprint 2 — Event Dashboard & Invitation UI
- [ ] **`TASK-212`** **Event Creation Dialog & EventType Selector**
  - **Feature**: #6
  - **Target Files**: `frontend/src/features/event/components/CreateEventModal.tsx`
  - **Acceptance Criteria**: Form allows selecting `EventType` (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM), dates, location.
- [ ] **`TASK-213`** **Event List & Event Detail Dashboard UI**
  - **Feature**: #9
  - **Target Files**: `frontend/src/features/event/pages/EventListPage.tsx`, `EventDetailPage.tsx`
  - **Acceptance Criteria**: Displays event cards, status badges, member list, navigation tabs (Plans, Members, Chat, Settings).
- [ ] **`TASK-214`** **Member Invitation Modal & Pending List UI**
  - **Feature**: #7
  - **Target Files**: `frontend/src/features/event/components/InviteMemberModal.tsx`
  - **Acceptance Criteria**: Allows sending email/link invites, displays pending invitations list with status (Pending/Accepted/Declined).
- [ ] **`TASK-215`** **Interactive Map Component (Mapbox Integration)**
  - **Feature**: #19
  - **Target Files**: `frontend/src/components/map/MapView.tsx`
  - **Acceptance Criteria**: Renders markers for plan stops, centers camera dynamically, shows popup details on marker click.

### Sprint 3 — Plan Builder & Voting Dashboard
- [ ] **`TASK-314`** **Manual Plan Builder Component (Drag & Drop)**
  - **Feature**: #11, #12
  - **Target Files**: `frontend/src/features/plan/components/PlanBuilder.tsx`
  - **Acceptance Criteria**: Allows adding stops with Google Places autocomplete, reordering stops via drag & drop, editing cost/notes.
- [ ] **`TASK-315`** **Voting Dashboard & Comment Thread UI**
  - **Feature**: #13
  - **Target Files**: `frontend/src/features/plan/components/PlanVotingCard.tsx`
  - **Acceptance Criteria**: Displays UP/DOWN/NEUTRAL buttons, vote count progress bar, comment thread, "Send for Vote" button.
- [ ] **`TASK-316`** **Plan Confirmation & Status Badge UI**
  - **Feature**: #14
  - **Target Files**: `frontend/src/features/plan/components/PlanHeader.tsx`
  - **Acceptance Criteria**: Shows status badge (Draft, Voting, Confirmed). Renders "Confirm Plan" button only for Event Owner.

---

## 🤝 Handover & Review Guidelines (Person 4)

1. **Buddy / Backup**: `Person 5` (Frontend Dev B)
2. **Task Completion**: Run `npm run lint` and `npm run test`. Push branch `feature/TASK-xxx` and tag `@FE-B` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
