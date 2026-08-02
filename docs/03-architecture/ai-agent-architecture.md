# AI Multi-Agent Architecture (Nhóm 4)

## 1. Tổng quan
Hệ thống dùng mô hình **Orchestrator–Worker** trên nền **LangGraph**: 1 agent điều phối (orchestrator) nhận yêu cầu, quyết định gọi sub-agent nào, tổng hợp kết quả trả về.

```
                     ┌─────────────────────┐
         user/UI ────▶│   Orchestrator Agent  │
                      │   (state machine)      │
                      └──────────┬────────────┘
                                 │ điều phối theo intent
        ┌──────────┬───────────┼───────────┬───────────┬──────────┐
        ▼          ▼           ▼           ▼           ▼          ▼
   ┌─────────┐┌─────────┐┌───────────┐┌─────────┐┌──────────┐┌───────────┐
   │Location   ││Research   ││ Plan        ││Booking    ││Cost         ││Conflict     │
   │Agent (9.2) ││Agent (9.5) ││ Agent (9.3)  ││Agent (9.1) ││Agent (9.9)  ││Resolver(9.6)│
   └─────────┘└─────────┘└───────────┘└─────────┘└──────────┘└───────────┘
        │          │           │           │           │          │
        └──────────┴───────────┴─────┬─────┴───────────┴──────────┘
                                      ▼
                          Ghi kết quả/đề xuất → DB (qua service Nhóm 2)
```

`Note Agent (9.4)` và `Chat Agent (9.7)` hoạt động song song, không nhất thiết đi qua orchestrator mỗi lần (9.7 có thể là 1 agent hội thoại độc lập có tool-calling tới các agent khác khi cần).

## 1.1 Routing theo loại sự kiện (EventType)

Orchestrator nhận `eventType` từ context event và điều chỉnh chiến lược gọi sub-agent phù hợp:

| EventType | Luồng Agent chính | Ghi chú |
|---|---|---|
| `TRAVEL` | Location → Research → Plan → Booking → Cost | Luồng mặc định, lên lịch trình nhiều ngày |
| `DINING` | Location (filter: nhà hàng/quán ăn) → Research (menu, review) → Plan (chọn quán + giờ) → Booking (đặt bàn) | Gợi ý **món ăn** dựa trên sở thích nhóm, dị ứng, ngân sách |
| `HANGOUT` | Location (filter: cafe/bar) → Plan (chọn quán + giờ) | Luồng ngắn, ít bước |
| `ENTERTAINMENT` | Location (filter: khu vui chơi, karaoke, bowling...) → Research (giá vé, khung giờ) → Plan → Booking | Gợi ý hoạt động phù hợp số người, độ tuổi |
| `SIGHTSEEING` | Location (filter: bảo tàng, di tích, triển lãm) → Research (giờ mở cửa, giá vé, tips) → Plan → Cost | Tối ưu tuyến đường tham quan |
| `CUSTOM` | Chat Agent xử lý tự do, user tự thêm stop thủ công | Orchestrator ở chế độ trợ lý, không tự động generate full plan |

> **Lưu ý**: Location Agent dùng chung cho mọi loại sự kiện, nhưng nhận thêm tham số `category` filter (RESTAURANT, CAFE, ENTERTAINMENT, ATTRACTION...) để thu hẹp kết quả Google Places phù hợp context.

## 2. Vai trò từng Agent
| Agent | Input chính | Output | Ghi chú |
|---|---|---|---|
| Orchestrator (9.9) | Yêu cầu người dùng (text/action) + context event | Quyết định route + tổng hợp kết quả | State machine LangGraph, có thể human-in-the-loop |
| Location Agent (9.2) | Sở thích, ngân sách, khu vực | Danh sách địa điểm gợi ý | Gọi Nhóm 3 (Google Places), có cache. Nhận thêm tham số `category` filter. |
| Research Agent (9.5) | Địa điểm cụ thể | Thông tin chi tiết, review tổng hợp | Có thể dùng RAG (pgvector) nếu có dữ liệu tích luỹ. Với sự kiện DINING có thể lấy thông tin menu/giá. |
| Plan Agent (9.3) | Danh sách địa điểm + ràng buộc thời gian | Lịch trình theo ngày + ngân sách sơ bộ | Tích hợp quản lý ngân sách theo yêu cầu #9.3. Với các sự kiện phi TRAVEL (như DINING, HANGOUT), output đơn giản hơn (chọn quán + giờ, không cần lịch trình nhiều ngày). |
| Booking Agent (9.1) | Địa điểm/khách sạn đã chọn | Link đặt chỗ sẵn (không tự đặt hộ) | Chỉ đưa link, không thực hiện giao dịch thay user (an toàn + đúng scope MVP) |
| Note Agent (9.4) | Loại chuyến đi, thời tiết (Nhóm 3) | Checklist/lưu ý khi đi chơi | |
| Conflict Resolver (9.6) | Kết quả vote (nhiều ý kiến trái chiều) | Đề xuất phương án dung hoà | Xem mục 4 |
| Cost Agent (9.9 — tính chi phí) | Danh sách stop + giá ước tính | Tổng chi phí, chia đều (liên kết Nhóm 7) | Ưu tiên tính bằng code thường, chỉ dùng LLM để trích xuất giá từ text không có cấu trúc |
| Chat Agent (9.7) | Hội thoại tự do của user | Trả lời + có thể gọi tool tới agent khác | Có thể expose qua `/ai/chat`, dùng streaming (SSE/WebSocket) |

## 3. State & Checkpoint
- Dùng LangGraph state để lưu: `eventId`, `eventType`, `userIntent`, `retrievedPlaces`, `draftPlan`, `budgetConstraint`, `conversationHistory`.
- Checkpoint theo `eventId` (không theo session tạm) để nhiều thành viên trong event có thể tiếp tục cùng 1 ngữ cảnh AI đang xử lý.

## 4. Vote & Confirm — áp dụng cho MỌI loại Plan

Luồng Vote → Confirm **áp dụng bình đẳng** cho cả Plan do AI tạo lẫn Plan tạo thủ công (#12):

```
Plan tạo bởi AI ─────┐
                      ├──▶ status = DRAFT ──▶ VOTING ──▶ CONFIRMED / ARCHIVED
Plan tạo thủ công ────┘
```

### Quy tắc:
- **Mọi Plan** (dù AI hay thủ công) khi tạo đều có `status = DRAFT`.
- Người tạo plan (Owner hoặc Member) bấm **"Gửi cho nhóm vote"** → `status = VOTING` → notification tới tất cả member.
- Member vote (UP / DOWN / NEUTRAL) + comment góp ý.
- Nếu vote phân tán → Conflict Resolver Agent có thể được gọi để đề xuất dung hòa (chỉ áp dụng nếu user chọn nhờ AI hỗ trợ).
- **Chỉ Owner** mới có quyền xác nhận → `status = CONFIRMED`.
- AI **không tự động chốt plan cuối cùng** — AI hỗ trợ ra quyết định, **không thay quyền quyết định của người dùng**.

### Edge case:
- Event chỉ có **1 người** → cho phép skip voting, confirm trực tiếp.
- Một event có thể có **nhiều plan DRAFT song song** (VD: 1 plan AI đề xuất + 1 plan member tự tạo) → nhóm vote chọn plan tốt nhất.

### Plan thủ công (#12) — luồng chi tiết:
1. **Bất kỳ Member nào** (không chỉ Owner) có thể tạo plan thủ công.
2. Thêm từng stop bằng tay — hỗ trợ autocomplete từ Google Places (Nhóm 3).
3. Plan lưu với `status = DRAFT`, `isAiGenerated = false`.
4. Khi sẵn sàng → người tạo bấm "Gửi cho nhóm vote" → `VOTING`.
5. Sau khi CONFIRMED, plan thủ công **bình đẳng hoàn toàn** với plan AI: export PDF, xem bản đồ, chia chi phí, nhận notification.

## 5. Bảo mật đầu vào (phối hợp Nhóm 1 + Nhóm 4, xem thêm `05-security/security-guidelines.md`)
- Mọi input tự do từ user (chat, ghi chú, tên địa điểm tự nhập) đi qua bước **sanitize + validate schema** trước khi đưa vào prompt.
- Không nối trực tiếp input người dùng vào system prompt mà không có ranh giới rõ ràng (dùng cấu trúc message role user/system tách biệt của LLM API, không tự ghép chuỗi).
- Giới hạn độ dài input, giới hạn số lần gọi tool/agent trong 1 phiên (tránh lạm dụng gây tốn chi phí hoặc DoS).
- Output từ LLM trước khi lưu DB hoặc hiển thị **luôn được validate qua Zod schema** — không tin dữ liệu LLM trả về là đúng định dạng 100%.

## 6. Theo dõi chi phí (liên kết Nhóm 6)
- Mỗi lần gọi Agent ghi log vào bảng `agent_logs` (input/output tokens, thời gian, agent nào) — xem `database-schema.md`.
- Admin Dashboard (Nhóm 6) tổng hợp chi phí theo user/theo ngày từ bảng này để tính giới hạn lượt dùng (nếu triển khai #10 sau này).

## 7. Quyết định còn mở (cần chốt ở tuần đầu — ghi ADR)
- [ ] LangGraph.js (Node, cùng stack Backend) hay LangGraph Python (tách service riêng)?
- [ ] Model mặc định: Dùng `deepseek-chat` (DeepSeek-V3) cho toàn bộ để tối ưu chi phí và tốc độ, hay dùng `deepseek-reasoner` (DeepSeek-R1) cho các agent phức tạp cần suy luận (Plan Agent 9.3, Conflict Resolver 9.6)?
- [ ] Chat Agent dùng streaming qua WebSocket (Socket.IO) hay SSE — ảnh hưởng cách Frontend implement màn hình chat (15).
