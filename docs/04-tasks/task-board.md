# Task Board & Sprint Plan — 6 người chạy song song

> Theo dõi thực tế bằng **GitHub Projects (Kanban)**, file này là bản tóm tắt. Board có **6 cột dọc theo người** (không phải theo nhóm tính năng) để nhìn rõ ai đang làm gì, ai đang rảnh.

## 1. Sprint 0 — Contract Session (ngày 1–2, bắt buộc cả 6 người)
Xem chi tiết quy trình ở [contract-first-workflow.md](../01-workflow/contract-first-workflow.md).
- [ ] Chốt DB schema khởi điểm
- [ ] Chốt OpenAPI spec toàn bộ endpoint
- [ ] Backend Dev A tạo controller skeleton + chạy migration
- [ ] Security dựng CI/CD + Docker Compose
- [ ] Frontend + AI Engineer setup mock (MSW / fixture data)

**Mốc ra khỏi Sprint 0**: contract đã push lên `main`, mọi người có thể code song song từ đây.

## 2. Sprint 1–4 — 6 track chạy song song

| Track | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
|---|---|---|---|---|
| **BE-A (Core)** | Auth hoàn chỉnh | Event/Plan CRUD + phân quyền | Vote + Plan Stop | Hardening + test coverage |
| **BE-B (Platform)** | Setup External API + cache | Hoàn thiện Places/Weather/Currency | Notification + Export PDF | Admin Dashboard |
| **AI Engineer** | Orchestrator skeleton + mock data | Location Agent, Note Agent | Plan Agent, Cost Agent, Conflict Resolver | Chat Agent + hoàn thiện, nối DB thật |
| **FE-A (Core)** | UI Auth (mock API) | UI Event/Plan/Vote (mock API) | Nối API thật (Integration Day) + Checklist UI | Polish + test |
| **FE-B (Growth)** | Landing page + i18n khung | UI AI Chat (mock) | Nối AI Chat thật + chia chi phí UI | Admin Dashboard UI |
| **Security/DevOps** | CI/CD + Docker + threat model | Review PR Auth (BE-A) | Review PR AI Agent (prompt injection) | Pentest toàn hệ thống trước demo |

> Mỗi ô là backlog riêng của người đó trong sprint — không có ô nào phụ thuộc phải "chờ" ô khác xong mới bắt đầu, nhờ contract đã chốt ở Sprint 0. Chi tiết từng dòng, xem file task riêng của từng người.

## 3. Bảng theo dõi (cập nhật hàng tuần bởi từng người)

| Người | File task chi tiết | Trạng thái tuần này | Blocker |
|---|---|---|---|
| Backend Dev A | [person-1-backend-core.md](person-1-backend-core.md) | 🔲 To Do | — |
| Backend Dev B | [person-2-backend-platform.md](person-2-backend-platform.md) | 🔲 To Do | — |
| AI Engineer | [person-3-ai-engineer.md](person-3-ai-engineer.md) | 🔲 To Do | — |
| Frontend Dev A | [person-4-frontend-core.md](person-4-frontend-core.md) | 🔲 To Do | — |
| Frontend Dev B | [person-5-frontend-growth.md](person-5-frontend-growth.md) | 🔲 To Do | — |
| Security/DevOps | [person-6-security-devops.md](person-6-security-devops.md) | 🔲 To Do | — |

Chú thích: 🔲 To Do · 🟡 In Progress · 🔵 In Review · ✅ Done · 🔴 Blocked

## 4. Điểm đồng bộ bắt buộc giữa các track (không thể tránh phụ thuộc 100%, nhưng giảm tối đa)
| Thời điểm | Ai gặp nhau | Vì sao |
|---|---|---|
| Cuối Sprint 1 | BE-A ↔ AI Engineer | Đối chiếu schema Event/Plan thật vs mock đã dùng |
| Cuối Sprint 1 | BE-A ↔ FE-A | Integration Day đầu tiên — Auth thật |
| Cuối Sprint 2 | BE-B ↔ AI Engineer | Location/Note Agent nối API thật của Nhóm 3 |
| Cuối Sprint 3 | AI Engineer ↔ FE-B | Chat Agent nối UI thật (streaming) |
| Xuyên suốt | Security ↔ tất cả | Review PR nhạy cảm (Auth, AI, Admin) trong 24h, không chặn tiến độ |

## 5. Quy tắc quản lý task (giữ nguyên)
- 1 Issue = 1 task cụ thể, có **Acceptance Criteria** rõ ràng.
- Task > 3 ngày công → tách sub-task.
- Task `Blocked` → ghi rõ đang chờ gì/chờ ai trong comment Issue, báo ngay ở daily update, đừng để tự "im lặng chờ".
- Cuối mỗi sprint: mỗi người demo phần mình (kể cả AI Engineer demo trên mock nếu Backend chưa xong thật) — không đợi đủ mọi thứ mới demo.
