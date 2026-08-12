# Testing Guide

## 1. Mức test & công cụ
| Loại | Công cụ | Bắt buộc cho |
|---|---|---|
| Unit test | pytest (BE), Vitest (FE) | Service/business logic, util function, Agent logic |
| Integration test | pytest + httpx.AsyncClient (BE, dùng test DB riêng) | Endpoint API quan trọng (Auth, Event/Plan/Vote CRUD, AI orchestrator) |
| Component test | Vitest + React Testing Library | Component có logic/state phức tạp (form, vote UI) |
| E2E (nếu còn thời gian) | Playwright | Luồng chính: đăng nhập → tạo event → tạo plan → vote |

## 2. Coverage tối thiểu (khuyến nghị, CI cảnh báo nếu dưới ngưỡng)
| Module | Ngưỡng coverage |
|---|---|
| Nhóm 1 (Auth) | ≥ 70% |
| Nhóm 2 (Core CRUD) | ≥ 70% |
| Nhóm 4 (AI Agent logic không gọi LLM thật) | ≥ 60% |
| Nhóm 3, 5, 6, 7 | ≥ 50% |

> Coverage là chỉ số tham khảo, không phải mục tiêu tự thân — ưu tiên test đúng case quan trọng hơn là chạy theo %.

## 3. Quy tắc đặt tên test
```
test_<tên_module>.py          // unit/integration test đi kèm module
test_<tên_module>_e2e.py       // e2e test
```
- `class` = nhóm các test liên quan, `def test_` = mô tả hành vi theo dạng "should ... when ...":
```python
class TestEventService:
    class TestCreateEvent:
        def test_should_create_event_and_set_creator_as_owner(self, ...): ...
        def test_should_raise_error_when_end_date_before_start_date(self, ...): ...
```

## 4. Cấu trúc test: Arrange – Act – Assert (AAA)
```python
async def test_should_raise_403_when_viewer_tries_to_edit_plan(self, async_client):
    # Arrange
    viewer = create_mock_member(role="VIEWER")
    dto = {"title": "New title"}

    # Act
    response = await async_client.patch(f"/api/v1/events/{event_id}/plans/{plan_id}", json=dto,
                                         headers=viewer_auth_header(viewer))

    # Assert
    assert response.status_code == 403
```

## 5. Test riêng cho AI Agent (Nhóm 4)
Vì gọi LLM thật tốn chi phí + không deterministic, tách 2 lớp test:

### a) Test logic thuần (không gọi LLM thật) — bắt buộc
- Mock LLM client, trả về response giả định (fixture JSON cố định).
- Test: orchestrator có route đúng sang sub-agent tương ứng không, agent có validate/parse đúng output theo Pydantic schema không, có xử lý đúng khi LLM trả JSON sai định dạng không (fallback/retry).
```python
async def test_should_route_to_plan_agent_when_intent_is_create_plan(self):
    mock_llm.return_value = {"intent": "create_plan", "payload": {...}}
    result = await orchestrator.run(input)
    plan_agent.generate.assert_called_once()
```

### b) Test tích hợp với LLM thật (không chạy trong CI mặc định) — tuỳ chọn
- Đánh dấu bằng tag riêng (VD `test:ai-live`), chỉ chạy thủ công hoặc theo lịch (không chạy mỗi PR để tránh tốn chi phí/API key trong CI công khai).
- Dùng để đánh giá chất lượng output định kỳ (prompt regression check), không phải test pass/fail cứng nhắc.

## 6. Integration test API
- Dùng database test riêng (Postgres container riêng qua `docker-compose.test.yml`), seed data trước mỗi test suite, rollback/truncate sau mỗi test.
- Không test integration nhắm vào database dev/production.
```python
class TestCreateEvent:
    async def test_should_return_401_when_no_token_provided(self, async_client):
        dto = {"name": "Test Event", "event_type": "DINING"}
        response = await async_client.post("/api/v1/events", json=dto)
        assert response.status_code == 401
```

## 7. Bắt buộc trong CI (GitHub Actions)
- Mọi PR chạy: `ruff check` + `mypy` → `pytest` unit test → `pytest` integration test (dùng test DB trong container) → `docker build`.
- PR fail bất kỳ bước nào → không cho merge (branch protection rule yêu cầu check "CI / test" pass).

## 8. Khi nào **không cần** viết test
- Code cấu hình thuần (VD `backend/app/main.py` FastAPI app bootstrap), UI tĩnh không có logic (landing page tĩnh Nhóm 7) — ưu tiên thời gian cho logic nghiệp vụ và AI Agent.
