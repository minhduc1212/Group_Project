# Person 3 — AI Engineer (Multi-Agent System)

**Sở hữu**: Toàn bộ N4 — trọng tâm đồ án. Chạy song song từ Sprint 1 bằng **mock data**, không chờ Backend code logic thật.
Xem kiến trúc chi tiết ở [ai-agent-architecture.md](../03-architecture/ai-agent-architecture.md) trước khi bắt đầu.

## Sprint 0 — Contract
- [ ] Tham gia chốt SQLAlchemy/Pydantic schemas (đặc biệt `Event`, `Plan`, `PlanStop`, `PlanVote`, `AgentLog`) — góp ý field `category` và `metadata` JSON cho Agent
- [ ] Tạo `fixtures/mock_events.json`, `fixtures/mock_places.json` đúng theo contract đã chốt, dùng để dev/test Agent không cần chờ Backend
- [ ] Setup LangGraph Python (`langgraph`) & SDK DeepSeek (`langchain-deepseek` / `openai` SDK): `deepseek-chat` (intent, tool calling) vs `deepseek-reasoner` (planning, conflict resolution, menu suggestion)

## Sprint 1 — Orchestrator + EventType Routing (LangGraph Python)
- [ ] Orchestrator Agent *(#23)*: Pydantic State schema, **routing theo EventType** (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM), `recursion_limit` giới hạn số bước
- [ ] Test logic orchestrator với Pytest + mock LLM response (chưa cần gọi API thật liên tục — tiết kiệm chi phí lúc dev)
- **Đồng bộ cuối sprint**: đối chiếu schema mock đã dùng với schema thật của Backend Dev A, chỉnh nếu lệch.

## Sprint 2 — Location & Note Agent
- [ ] Agent tìm địa điểm *(#24)* — gọi API thật của Backend Dev B (Places với category filter: RESTAURANT, CAFE, ENTERTAINMENT, ATTRACTION) ngay khi có
- [ ] Agent lưu ý khi đi chơi *(#28)* — dùng data thời tiết Backend Dev B
- [ ] Agent research *(#25)* — gợi ý menu/món ăn (DINING), giá vé & tips (ENTERTAINMENT, SIGHTSEEING)

## Sprint 3 — Plan, Cost, Conflict Resolver
- [ ] Agent tạo plan + quản lý ngân sách *(#26)* — tạo lịch trình (TRAVEL), chọn quán + món (DINING), hoạt động (ENTERTAINMENT)
- [ ] Agent tính chi phí *(#29)* — ưu tiên tính bằng Python code thuần, LLM chỉ trích giá từ text
- [ ] Agent phân giải xung đột *(#30)* — đọc kết quả vote, dùng `deepseek-reasoner` đề xuất phương án dung hòa (Human-in-the-loop)
- [ ] Agent booking *(#27)* — chỉ trả link đặt phòng/đặt bàn/đặt vé, không tự đặt hộ

## Sprint 4 — Chat Agent + Nối thật (FastAPI WebSockets / SSE)
- [ ] AI Agent chat *(#31)*, hỗ trợ streaming (FastAPI WebSockets hoặc `EventSourceResponse` SSE)
- [ ] Nối toàn bộ Agent với DB thật qua SQLAlchemy AsyncSession (thay mock hoàn toàn)
- [ ] Ghi log đầy đủ vào `AgentLog` (tokens, duration_ms, agent_name) cho Admin Dashboard
- [ ] Demo full flow: tạo event → AI đề xuất plan → vote → conflict resolver → confirm

## Bảo mật bắt buộc (phối hợp Security/DevOps — Person 6)
- [ ] Validate/sanitize input trước khi vào prompt qua Pydantic & bleach (không nối chuỗi thô)
- [ ] Output LLM validate qua Pydantic schema trước khi lưu DB
- [ ] Rate limit `/api/v1/ai/*`, giới hạn recursion_limit trong graph

## Định nghĩa Done chung
- Mỗi agent có Pytest unit test với mock LLM (không phụ thuộc gọi API thật trong CI)
- Đã qua review Security cho input/output validation

## Không được tự ý làm khi chưa báo
- Đổi Pydantic state schema Orchestrator ảnh hưởng Chat Agent (Person 5 build UI dựa trên đó) → báo `#contract-changes`.
