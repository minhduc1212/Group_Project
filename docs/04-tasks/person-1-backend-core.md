# Person 1 — Backend Dev A (Core Domain)

**Sở hữu**: Auth (N1) + Event/Plan/Vote (N2) — người thiết kế schema DB gốc dùng chung toàn hệ thống.
**Tham gia bắt buộc**: Contract Session (Sprint 0), Integration Day cuối Sprint 1.

## Sprint 0 — Contract
- [ ] Đề xuất & chốt DB schema (`03-architecture/database-schema.md`) cùng team (bao gồm `EventType`, `Invitation`, `StopCategory`, `metadata` JSON)
- [ ] Chốt OpenAPI spec `/auth/*`, `/events/*`, `/invitations/*`, `/plans/*`, `/votes/*` cùng team
- [ ] Tạo controller skeleton (chưa cần logic thật) + chạy migration DB thật đầu tiên
- [ ] Setup `AuthGuard`/`RolesGuard` khung sườn để người khác biết interface (dù logic bên trong chưa xong)

## Sprint 1 — Auth hoàn chỉnh
- [ ] Đăng nhập Google/Facebook OAuth2 *(#1)*
- [ ] Đăng ký + hash password bcrypt *(#2)*
- [ ] Quên mật khẩu *(#3)*
- [ ] Refresh token, logout *(#5)*
- [ ] Test đầy đủ `auth.e2e-spec.ts`
- **Mốc cuối sprint**: Auth thật deploy ở `dev`/`staging` → Frontend Dev A tắt mock, nối thật (Integration Day)

## Sprint 2 — Event/Plan CRUD + phân quyền + Invitations
- [ ] CRUD Event với `EventType` (TRAVEL, DINING, HANGOUT, ENTERTAINMENT, SIGHTSEEING, CUSTOM) *(#6)*
- [ ] Quản lý lời mời (Invitations API): gửi lời mời qua email/userId, accept/decline *(#7)*
- [ ] `RolesGuard` Owner/Member/Viewer đầy đủ logic — ma trận quyền:

| Hành động | Owner | Member | Viewer |
|---|---|---|---|
| Xem event/plan | ✅ | ✅ | ✅ |
| Tạo/sửa plan (thủ công & AI) | ✅ | ✅ | ❌ |
| Vote plan | ✅ | ✅ | ❌ |
| Mời thành viên | ✅ | ❌ | ❌ |
| Xoá event | ✅ | ❌ | ❌ |
| Chuyển status plan (CONFIRMED) | ✅ | ❌ | ❌ |

- [ ] Tạo/sửa Plan thủ công *(#11, #12)* — lưu `isAiGenerated = false`, `status = DRAFT`
- [ ] API chuyển trạng thái Plan (`PATCH /status`): DRAFT → VOTING → CONFIRMED (áp dụng cho cả plan AI và plan thủ công)
- [ ] Tạo/xem/sửa Profile *(#4)*

## Sprint 3 — Vote + Plan Stop + Metadata
- [ ] Vote cho Plan (UP / DOWN / NEUTRAL), tổng hợp kết quả vote *(#13, #14)*
- [ ] Chỉnh sửa thứ tự / thêm / xoá Plan Stop (`PlanStop` với `category` và `metadata` JSON) *(#12)*
- [ ] Lưu danh sách yêu thích *(#15)*
- **Đồng bộ**: AI Engineer cần API `PATCH /plans/:id` và `POST /plans` ổn định để Plan Agent ghi kết quả — xác nhận response shape không đổi trước sprint này.

## Sprint 4 — Hardening
- [ ] Test coverage ≥ 70% toàn bộ module Auth + Event/Plan/Vote/Invitation
- [ ] Xử lý toàn bộ `[blocking]` comment còn tồn đọng từ review Security
- [ ] Rà soát lại N-query, index DB

## Định nghĩa Done chung mỗi task
- Swagger doc đầy đủ, test pass, đã qua review Security cho phần Auth/phân quyền (xem `05-security/security-guidelines.md`)

## Không được tự ý làm khi chưa báo
- Đổi field/bảng trong schema Prisma → báo `#contract-changes`, AI Engineer & Backend Dev B đang phụ thuộc trực tiếp.
