# Testing Guide

## 1. Mức test & công cụ
| Loại | Công cụ | Bắt buộc cho |
|---|---|---|
| Unit test | Jest (BE), Vitest (FE) | Service/business logic, util function, Agent logic |
| Integration test | Jest + Supertest (BE, dùng test DB riêng) | Endpoint API quan trọng (Auth, Event/Plan/Vote CRUD, AI orchestrator) |
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
<tên-file-gốc>.spec.ts     // unit/integration test đi kèm module
<tên-file-gốc>.e2e-spec.ts  // e2e test
```
- `describe` = tên class/function đang test, `it`/`test` = mô tả hành vi theo dạng "should ... when ...":
```ts
describe('EventService', () => {
  describe('createEvent', () => {
    it('should create event and set creator as OWNER', async () => { ... });
    it('should throw BadRequestException when endDate is before startDate', async () => { ... });
  });
});
```

## 4. Cấu trúc test: Arrange – Act – Assert (AAA)
```ts
it('should throw ForbiddenException when a VIEWER tries to edit plan', async () => {
  // Arrange
  const viewer = createMockMember({ role: 'VIEWER' });
  const dto = { title: 'New title' };

  // Act
  const act = () => planService.updatePlan(planId, dto, viewer);

  // Assert
  await expect(act).rejects.toThrow(ForbiddenException);
});
```

## 5. Test riêng cho AI Agent (Nhóm 4)
Vì gọi LLM thật tốn chi phí + không deterministic, tách 2 lớp test:

### a) Test logic thuần (không gọi LLM thật) — bắt buộc
- Mock LLM client, trả về response giả định (fixture JSON cố định).
- Test: orchestrator có route đúng sang sub-agent tương ứng không, agent có validate/parse đúng output theo Zod schema không, có xử lý đúng khi LLM trả JSON sai định dạng không (fallback/retry).
```ts
it('should route to plan agent when intent is "create_plan"', async () => {
  mockLLM.mockResolvedValueOnce({ intent: 'create_plan', payload: {...} });
  const result = await orchestrator.run(input);
  expect(planAgent.generate).toHaveBeenCalled();
});
```

### b) Test tích hợp với LLM thật (không chạy trong CI mặc định) — tuỳ chọn
- Đánh dấu bằng tag riêng (VD `test:ai-live`), chỉ chạy thủ công hoặc theo lịch (không chạy mỗi PR để tránh tốn chi phí/API key trong CI công khai).
- Dùng để đánh giá chất lượng output định kỳ (prompt regression check), không phải test pass/fail cứng nhắc.

## 6. Integration test API
- Dùng database test riêng (Postgres container riêng qua `docker-compose.test.yml`), seed data trước mỗi test suite, rollback/truncate sau mỗi test.
- Không test integration nhắm vào database dev/production.
```ts
describe('POST /events (e2e)', () => {
  it('should return 401 when no token provided', () => {
    return request(app.getHttpServer()).post('/events').send(dto).expect(401);
  });
});
```

## 7. Bắt buộc trong CI (GitHub Actions)
- Mọi PR chạy: `lint` → `unit test` → `integration test` (dùng test DB trong container) → `build`.
- PR fail bất kỳ bước nào → không cho merge (branch protection rule yêu cầu check "CI / test" pass).

## 8. Khi nào **không cần** viết test
- Code cấu hình thuần (VD `main.ts` bootstrap NestJS), UI tĩnh không có logic (landing page tĩnh Nhóm 7) — ưu tiên thời gian cho logic nghiệp vụ và AI Agent.
