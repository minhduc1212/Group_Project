# 👤 Person 3 — Nguyễn Tùng Dương & Tạ Quang Huy (AI Agent Team: LangGraph & Integration)

> **Người phụ trách**: 
> - **Nguyễn Tùng Dương** (AI Agent Lead: Architect, LangGraph State, DeepSeek V3/R1 Orchestrator & Reasoning Agents)
> - **Tạ Quang Huy** (AI Agent Integration: Tool Calling, Fixtures Data & Backend API Bridge)
> **Sở hữu**: Toàn bộ N4 — trọng tâm đồ án. Chạy song song từ Sprint 1 bằng **mock data / fixtures**, không chờ Backend code logic thật.
> Xem kiến trúc chi tiết ở [ai-agent-architecture.md](../03-architecture/ai-agent-architecture.md).

---

## 📊 Progress Tracker

| Sprint | Task Count | Người phụ trách | Done | Status |
|---|---|---|---|---|
| **Sprint 0** | 1 Task | Nguyễn Tùng Dương & Tạ Quang Huy | 0/1 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | Nguyễn Tùng Dương | 0/2 | 🔲 To Do |
| **Sprint 2** | 3 Tasks | Nguyễn Tùng Dương | 0/3 | 🔲 To Do |
| **Sprint 3** | 4 Tasks | Nguyễn Tùng Dương | 0/4 | 🔲 To Do |
| **Sprint 4** | 3 Tasks | Nguyễn Tùng Dương & Tạ Quang Huy | 0/3 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — State & Fixture Data (Nguyễn Tùng Dương & Tạ Quang Huy)
- [ ] **`TASK-003`** `[AI Lead - Nguyễn Tùng Dương & Tạ Quang Huy]` **LangGraph State & Fixture Data Definition**
  - **Feature**: #23
  - **Target Files**: `backend/app/ai_agents/state.py`, `backend/app/ai_agents/fixtures/` (`mock_places.json`, `mock_plans.json`)
  - **Acceptance Criteria**: Define Pydantic `AgentState`. Mock fixtures validate cleanly against DB schemas.

### Sprint 1 — Orchestrator & DeepSeek Provider Setup (Nguyễn Tùng Dương)
- [ ] **`TASK-109`** `[AI Lead - Nguyễn Tùng Dương]` **LangGraph Orchestrator Skeleton**
  - **Feature**: #23
  - **Target Files**: `backend/app/ai_agents/orchestrator.py`
  - **Acceptance Criteria**: Graph builds state, routes intent to dummy sub-agents based on `EventType`, respects `recursion_limit=15`.
- [ ] **`TASK-110`** `[AI Lead - Nguyễn Tùng Dương]` **DeepSeek API Provider Wrapper**
  - **Feature**: #23, #31
  - **Target Files**: `backend/app/ai_agents/llm_provider.py`
  - **Acceptance Criteria**: Wraps `deepseek-chat` and `deepseek-reasoner` with retry logic, rate limiting, and token logging.

### Sprint 2 — Location, Research & Note Agents (Nguyễn Tùng Dương)
- [ ] **`TASK-209`** `[AI Lead - Nguyễn Tùng Dương]` **Location Agent Implementation**
  - **Feature**: #24
  - **Target Files**: `backend/app/ai_agents/agents/location_agent.py`
  - **Acceptance Criteria**: Receives category filter and preferences, queries `PlacesService`, returns top 5 structured place suggestions.
- [ ] **`TASK-210`** `[AI Lead - Nguyễn Tùng Dương]` **Research Agent Implementation**
  - **Feature**: #25
  - **Target Files**: `backend/app/ai_agents/agents/research_agent.py`
  - **Acceptance Criteria**: Fetches place reviews, generates menu suggestions for DINING, activity ticket prices for ENTERTAINMENT, opening hours for SIGHTSEEING.
- [ ] **`TASK-211`** `[AI Lead - Nguyễn Tùng Dương]` **Note Agent Implementation**
  - **Feature**: #28
  - **Target Files**: `backend/app/ai_agents/agents/note_agent.py`
  - **Acceptance Criteria**: Combines weather forecast with destination type to generate smart travel/hangout tips.

### Sprint 3 — Plan, Cost, Conflict & Booking Agents (Nguyễn Tùng Dương)
- [ ] **`TASK-307`** `[AI Lead - Nguyễn Tùng Dương]` **Plan Agent Implementation (DeepSeek-R1)**
  - **Feature**: #26
  - **Target Files**: `backend/app/ai_agents/agents/plan_agent.py`
  - **Acceptance Criteria**: Uses `deepseek-reasoner` to build optimal stop sequence, time allocation, and daily budget based on event type.
- [ ] **`TASK-308`** `[AI Lead - Nguyễn Tùng Dương]` **Cost Agent Implementation**
  - **Feature**: #29
  - **Target Files**: `backend/app/ai_agents/agents/cost_agent.py`
  - **Acceptance Criteria**: Calculates total budget, per-person split, and per-item breakdown using Python code.
- [ ] **`TASK-309`** `[AI Lead - Nguyễn Tùng Dương]` **Conflict Resolver Agent Implementation (DeepSeek-R1)**
  - **Feature**: #30
  - **Target Files**: `backend/app/ai_agents/agents/conflict_agent.py`
  - **Acceptance Criteria**: Analyzes vote comments and negative votes, generates a compromised draft plan resolving objections.
- [ ] **`TASK-310`** `[AI Lead - Nguyễn Tùng Dương]` **Booking Agent Implementation**
  - **Feature**: #27
  - **Target Files**: `backend/app/ai_agents/agents/booking_agent.py`
  - **Acceptance Criteria**: Returns direct booking URLs for hotels (Booking.com / Agoda), restaurant reservations, or activity tickets.

### Sprint 4 — Realtime AI Chat Engine & Token Logging (Nguyễn Tùng Dương & Tạ Quang Huy)
- [ ] **`TASK-401`** `[AI Lead - Nguyễn Tùng Dương]` **Chat Agent & Function Calling Setup**
  - **Feature**: #31
  - **Target Files**: `backend/app/ai_agents/agents/chat_agent.py`
  - **Acceptance Criteria**: Chat Agent routes user queries, calls sub-agent tools dynamically, maintains conversation state.
- [ ] **`TASK-402`** `[AI Integration - Tạ Quang Huy]` **FastAPI WebSocket & SSE Endpoints for Streaming**
  - **Feature**: #31
  - **Target Files**: `backend/app/api/v1/ai.py`
  - **Acceptance Criteria**: `/api/v1/ai/chat/stream` streams LLM output tokens in real-time using `EventSourceResponse` (SSE) or WebSockets.
- [ ] **`TASK-403`** `[AI Integration - Tạ Quang Huy]` **Agent Token Logging Service**
  - **Feature**: #36
  - **Target Files**: `backend/app/services/agent_logger.py`
  - **Acceptance Criteria**: Every LLM call logs `input_tokens`, `output_tokens`, `duration_ms`, `agent_name`, `user_id` to `agent_logs` table.

---

## 🤝 Handover & Review Guidelines (Person 3)

1. **Buddy / Backup**: **Tạ Quang Huy** (Backend Dev A & AI Integration)
2. **Task Completion**: Run `pytest backend/tests/test_agents.py` with mock LLM responses. Push branch `feature/TASK-xxx` and tag `@AI-Lead` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
