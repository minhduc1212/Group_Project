# Git Workflow

## 1. Mô hình branching: **GitHub Flow rút gọn** (không dùng Gitflow đầy đủ — quá nặng cho team 6 người/đồ án)

```
main                    → luôn deployable, bảo vệ (protected branch)
 └─ develop              → tích hợp trước khi lên main (tuỳ chọn, xem mục 4)
     └─ feature/xxx       → 1 branch / 1 task cụ thể
     └─ fix/xxx            → sửa bug
     └─ hotfix/xxx          → sửa khẩn trên main
```

### Quy tắc branch bảo vệ
- `main`: không push trực tiếp, bắt buộc PR + tối thiểu 1 approve + CI pass.
- `develop` (nếu dùng): PR + CI pass, không bắt buộc approve nếu team nhỏ nhưng khuyến khích.

## 2. Quy trình từ Task → PR → Merge

1. **Nhận task** từ [task-board.md](../04-tasks/task-board.md) (GitHub Projects / Issues), tự gán mình (assignee) + chuyển status `In Progress`.
2. **Tạo branch** từ `develop` (hoặc `main` nếu team không dùng `develop`), đặt tên theo [branch-naming.md](branch-naming.md).
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/N2-create-event
   ```
3. **Code + commit** theo [commit-convention.md](commit-convention.md), commit nhỏ, thường xuyên.
4. **Viết/chạy test** trước khi push (xem [testing-guide.md](../02-standards/testing-guide.md)). Không push code fail test.
5. **Cập nhật tài liệu (Post-Task Docs)**: Tra cứu [post-task-documentation.md](post-task-documentation.md) để cập nhật API spec, DB schema, ADR, và tick `[x]` hoàn thành task trên Task Board tương ứng trong cùng branch/PR.
6. **Rebase lên develop mới nhất** trước khi mở PR để tránh conflict lớn:
   ```bash
   git fetch origin
   git rebase origin/develop
   ```
7. **Push & mở Pull Request**, dùng template `.github/PULL_REQUEST_TEMPLATE.md`, điền mục Updated Docs, gắn label đúng nhóm (`group-2`, `ai`, `security`,...), link Issue (`Closes #23`).
8. **CI chạy tự động** (lint, test, build). PR không được merge nếu CI fail hoặc thiếu docs.
8. **Code review**: tối thiểu 1 approve theo [code-review-checklist.md](code-review-checklist.md). Có comment "changes requested" → tác giả sửa, không tự merge khi chưa resolve hết comment.
9. **Merge**: dùng **Squash and merge** vào `develop` (giữ lịch sử `main` sạch, 1 PR = 1 commit log rõ ràng). Xoá branch sau khi merge.
10. **Release lên `main`**: PR từ `develop` → `main` theo lịch (VD cuối mỗi sprint), tag version theo [Semantic Versioning](https://semver.org/) (`v0.1.0`, `v0.2.0`...).

## 3. Xử lý conflict
- Ưu tiên `rebase` thay vì `merge` khi cập nhật branch cá nhân từ `develop`, để lịch sử tuyến tính, dễ review.
- Nếu conflict phức tạp liên quan đến người khác (VD database-schema.md) → trao đổi trực tiếp trước khi tự resolve.

## 4. Có cần nhánh `develop` không?
- Team 6 người, đồ án ngắn hạn → **khuyến nghị bỏ qua `develop`, PR thẳng vào `main`** để đơn giản hoá, miễn là `main` luôn được bảo vệ bởi CI + review.
- Chỉ thêm `develop` nếu cần một môi trường staging tách biệt để demo trước khi release chính thức.

## 5. Emergency hotfix
```
git checkout main
git checkout -b hotfix/fix-jwt-expiry
# fix, commit, PR thẳng vào main, review nhanh, merge, sau đó merge ngược lại develop
```

## 6. Quy tắc chung
- Không commit trực tiếp lên `main`/`develop`.
- Không force-push lên branch dùng chung (`main`, `develop`). Force-push chỉ trên branch cá nhân (`feature/xxx` của chính mình) sau khi rebase.
- 1 PR nên giải quyết **1 vấn đề/task cụ thể** (tránh PR khổng lồ khó review — giới hạn khuyến nghị < 400 dòng diff, xem [code-review-checklist.md](code-review-checklist.md)).
