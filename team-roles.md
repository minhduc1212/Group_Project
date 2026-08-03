# Team & Roles — Mô hình 6 người làm song song

## 1. Nguyên tắc phân công (khác với "chia theo nhóm tính năng")
Cách chia theo Nhóm 1–7 tính năng (feature.md gốc) khiến người làm Nhóm 4 (AI) phải **chờ** Nhóm 2 xong mới có dữ liệu thật để code — không tối ưu cho 6 người có sẵn, muốn chạy song song ngay tuần 1.

Cách chia đúng kiểu công ty chuyên nghiệp: **chia theo vai trò (role)**, mỗi người sở hữu 1 mảng kỹ thuật **xuyên suốt toàn bộ dự án** (từ đầu đến cuối), làm việc song song với người khác thông qua **hợp đồng giao diện (contract)** chốt trước — không phải chờ nhau theo trình tự. Xem cơ chế chi tiết ở [contract-first-workflow.md](docs/01-workflow/contract-first-workflow.md).

## 2. 6 vai trò & người phụ trách

| # | Vai trò | Sở hữu mảng nào (theo tính năng gốc) | File task chi tiết |
|---|---|---|---|
| 1 | **Backend Dev A — Core Domain** | N1 (Auth) + N2 (Event/Plan/Vote) — schema DB gốc do người này thiết kế | [person-1-backend-core.md](docs/04-tasks/person-1-backend-core.md) |
| 2 | **Backend Dev B — Platform & Integration** | N3 (External API) + N5 (Notification/Export) + N6 (Admin) | [person-2-backend-platform.md](docs/04-tasks/person-2-backend-platform.md) |
| 3 | **AI Engineer** | N4 (toàn bộ Multi-Agent System) — làm song song từ tuần 1, dùng schema mock | [person-3-ai-engineer.md](docs/04-tasks/person-3-ai-engineer.md) |
| 4 | **Frontend Dev A — Core Flows** | UI cho Auth, Event, Plan, Vote, Checklist (N1, N2, N5 phần UI) | [person-4-frontend-core.md](docs/04-tasks/person-4-frontend-core.md) |
| 5 | **Frontend Dev B — AI Experience & Growth** | UI Chat AI, Landing, i18n, chia chi phí, Admin Dashboard UI (N4, N7, N6 phần UI) | [person-5-frontend-growth.md](docs/04-tasks/person-5-frontend-growth.md) |
| 6 | **Cyber Security & DevOps** | CI/CD, Docker, bảo mật xuyên suốt (review mọi PR nhạy cảm), pentest trước demo | [person-6-security-devops.md](docs/04-tasks/person-6-security-devops.md) |

> Nếu team thực tế nghiêng nhiều AI hơn, có thể đổi tỉ lệ thành 2 AI Engineer + gộp Backend Dev B làm kiêm Admin+Platform 1 mình — cấu trúc file vẫn giữ nguyên, chỉ đổi người gán.

## 3. Vì sao chia thế này chạy song song được?
| Vấn đề khi chia theo Nhóm cũ | Cách giải quyết khi chia theo Người |
|---|---|
| AI Engineer (N4) phải chờ Backend (N2) xong schema | Tuần 1 cả team chốt chung **1 buổi contract session**: schema Prisma + OpenAPI spec. AI Engineer code thẳng lên **mock server** dựng từ contract đó, không chờ Backend Dev A code xong thật |
| Frontend chờ Backend xong API mới code UI | Frontend dùng **MSW (Mock Service Worker)** mock response theo đúng OpenAPI contract, code UI song song, chỉ cần đổi `baseURL` khi Backend deploy thật |
| Security chỉ "review sau cùng" — dồn việc cuối dự án | Security có việc **riêng, chạy song song từ đầu**: dựng CI/CD, viết rule lint bảo mật, threat-model hệ AI Agent — không ngồi chờ có code mới bắt đầu |
| 1 người rảnh trong khi người khác bận vì phụ thuộc | Mỗi người có **backlog riêng đủ dùng cho cả dự án** trong file task của mình, không có giai đoạn "ngồi chờ" |

## 4. Ma trận phối hợp (RACI) — theo người thay vì theo nhóm

R = Responsible · A = Accountable · C = Consulted · I = Informed

| Đầu việc | BE-A (Core) | BE-B (Platform) | AI Engineer | FE-A (Core) | FE-B (Growth) | Security/DevOps |
|---|---|---|---|---|---|---|
| Contract API + Schema (tuần 1) | **R/A** | C | C | C | C | C |
| Auth (login/JWT) | **R/A** | I | I | C (gọi API) | I | **R** (review) |
| Event/Plan/Vote CRUD | **R/A** | I | C (đọc schema) | C (gọi API) | I | C |
| External API + cache | I | **R/A** | C (dùng data) | I | I | I |
| AI Multi-Agent | C (schema) | I | **R/A** | I | C (gọi API chat) | **R** (input validation review) |
| Notification/Export/Admin BE | I | **R/A** | C (log token) | I | C (UI admin) | C |
| UI Core Flows | C | I | I | **R/A** | C | I |
| UI AI Chat/Landing/i18n | I | I | C | C | **R/A** | I |
| CI/CD, Docker, Security | I | I | I | I | I | **R/A** |

## 5. Đồng bộ giữa 6 người
| Việc | Tần suất |
|---|---|
| Contract sync (đổi API/schema) | Bất cứ khi nào đổi — báo ngay kênh `#contract-changes`, không chờ họp |
| Daily update async | Mỗi ngày, 3 dòng: hôm qua/hôm nay/blocker |
| Weekly demo + đồng bộ contract | 1 buổi/tuần — mỗi người demo phần mình, đối chiếu contract có bị lệch không |
| Integration day | Cuối mỗi sprint — nối Frontend thật với Backend thật (thay mock), AI Engineer nối với DB thật |
