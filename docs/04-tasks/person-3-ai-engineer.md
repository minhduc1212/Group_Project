# 👤 Person 3 — AI Engineer (Multi-Agent System)

> **Sở hữu**: Toàn bộ N4 — trọng tâm đồ án. Chạy song song từ Sprint 1 bằng **mock data**, không chờ Backend code logic thật.
> Xem kiến trúc chi tiết ở [ai-agent-architecture.md](../03-architecture/ai-agent-architecture.md).

---

## 📊 Progress Tracker

| Sprint | Task Count | Done | Status |
|---|---|---|---|
| **Sprint 0** | 1 Task | 0/1 | 🔲 To Do |
| **Sprint 1** | 2 Tasks | 0/2 | 🔲 To Do |
| **Sprint 2** | 3 Tasks | 0/3 | 🔲 To Do |
| **Sprint 3** | 4 Tasks | 0/4 | 🔲 To Do |
| **Sprint 4** | 3 Tasks | 0/3 | 🔲 To Do |

---

## 🛠️ Detailed Sprint Backlog

### Sprint 0 — State & Fixture Data
- [ ] **`TASK-003`** **LangGraph State & Fixture Fixtures Definition**
  - **Feature**: #23
  - **Target Files**: `backend/app/ai_agents/state.py`, `backend/app/ai_agents/fixtures/` (`mock_places.json`, `mock_plans.json`)
  - **Acceptance Criteria**: Define Pydantic `AgentState`. Mock fixtures validate cleanly against DB schemas.

### Sprint 1 — Orchestrator & DeepSeek Provider Setup
- [ ] **`TASK-109`** **LangGraph Orchestrator Skeleton**
  - **Feature**: #23
  - **Target Files**: `backend/app/ai_agents/orchestrator.py`
  - **Acceptance Criteria**: Graph builds state, routes intent to dummy sub-agents based on `EventType`, respects `recursion_limit=15`.
- [ ] **`TASK-110`** **DeepSeek API Provider Wrapper**
  - **Feature**: #23, #31
  - **Target Files**: `backend/app/ai_agents/llm_provider.py`
  - **Acceptance Criteria**: Wraps `deepseek-chat` and `deepseek-reasoner` with retry logic, rate limiting, and token logging.

### Sprint 2 — Location, Research & Note Agents
- [ ] **`TASK-209`** **Location Agent Implementation**
  - **Feature**: #24
  - **Target Files**: `backend/app/ai_agents/agents/location_agent.py`
  - **Acceptance Criteria**: Receives category filter and preferences, queries `PlacesService`, returns top 5 structured place suggestions.
- [ ] **`TASK-210`** **Research Agent Implementation**
  - **Feature**: #25
  - **Target Files**: `backend/app/ai_agents/agents/research_agent.py`
  - **Acceptance Criteria**: Fetches place reviews, generates menu suggestions for DINING, activity ticket prices for ENTERTAINMENT, opening hours for SIGHTSEEING.
- [ ] **`TASK-211`** **Note Agent Implementation**
  - **Feature**: #28
  - **Target Files**: `backend/app/ai_agents/agents/note_agent.py`
  - **Acceptance Criteria**: Combines weather forecast with destination type to generate smart travel/hangout tips.

### Sprint 3 — Plan, Cost, Conflict & Booking Agents
- [ ] **`TASK-307`** **Plan Agent Implementation (DeepSeek-R1)**
  - **Feature**: #26
  - **Target Files**: `backend/app/ai_agents/agents/plan_agent.py`
  - **Acceptance Criteria**: Uses `deepseek-reasoner` to build optimal stop sequence, time allocation, and daily budget based on event type.
- [ ] **`TASK-308`** **Cost Agent Implementation**
  - **Feature**: #29
  - **Target Files**: `backend/app/ai_agents/agents/cost_agent.py`
  - **Acceptance Criteria**: Calculates total budget, per-person split, and per-item breakdown using Python code.
- [ ] **`TASK-309`** **Conflict Resolver Agent Implementation (DeepSeek-R1)**
  - **Feature**: #30
  - **Target Files**: `backend/app/ai_agents/agents/conflict_agent.py`
  - **Acceptance Criteria**: Analyzes vote comments and negative votes, generates a compromised draft plan resolving objections.
- [ ] **`TASK-310`** **Booking Agent Implementation**
  - **Feature**: #27
  - **Target Files**: `backend/app/ai_agents/agents/booking_agent.py`
  - **Acceptance Criteria**: Returns direct booking URLs for hotels (Booking.com / Agoda), restaurant reservations, or activity tickets.

### Sprint 4 — Realtime AI Chat Engine & Token Logging
- [ ] **`TASK-401`** **Chat Agent & Function Calling Setup**
  - **Feature**: #31
  - **Target Files**: `backend/app/ai_agents/agents/chat_agent.py`
  - **Acceptance Criteria**: Chat Agent routes user queries, calls sub-agent tools dynamically, maintains conversation state.
- [ ] **`TASK-402`** **FastAPI WebSocket & SSE Endpoints for Streaming**
  - **Feature**: #31
  - **Target Files**: `backend/app/api/v1/ai.py`
  - **Acceptance Criteria**: `/api/v1/ai/chat/stream` streams LLM output tokens in real-time using `EventSourceResponse` (SSE) or WebSockets.
- [ ] **`TASK-403`** **Agent Token Logging Service**
  - **Feature**: #36
  - **Target Files**: `backend/app/services/agent_logger.py`
  - **Acceptance Criteria**: Every LLM call logs `input_tokens`, `output_tokens`, `duration_ms`, `agent_name`, `user_id` to `agent_logs` table.

---

## 🤝 Handover & Review Guidelines (Person 3)

1. **Buddy / Backup**: `Person 1` (Backend Dev A)
2. **Task Completion**: Run `pytest backend/tests/test_agents.py` with mock LLM responses. Push branch `feature/TASK-xxx` and tag `@BE-A` on PR.
3. **Task Handover**: Follow 4 scenarios in [cross-team-collaboration.md](../01-workflow/cross-team-collaboration.md) Section 3.
