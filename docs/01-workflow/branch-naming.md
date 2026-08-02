# Branch Naming Convention

## Format chung
```
<type>/<mã-nhóm-hoặc-issue>-<mô-tả-ngắn-kebab-case>
```

## Các `type` hợp lệ
| Type | Dùng khi nào |
|---|---|
| `feature/` | Thêm tính năng mới |
| `fix/` | Sửa bug (không khẩn cấp) |
| `hotfix/` | Sửa khẩn trên `main` |
| `refactor/` | Tái cấu trúc code, không đổi hành vi |
| `chore/` | Việc vặt: cập nhật dependency, config, CI |
| `docs/` | Chỉ sửa tài liệu |
| `test/` | Chỉ thêm/sửa test |

## Quy tắc mô tả
- Toàn bộ chữ thường, phân tách bằng dấu gạch ngang (`kebab-case`).
- Ngắn gọn, tối đa ~5 từ, đủ hiểu nội dung không cần mở PR.
- Nên gắn mã nhóm tính năng (N1–N7, xem [feature.md gốc](../../feature.md) hoặc `04-tasks/`) hoặc số Issue để dễ trace.

## Ví dụ đúng
```
feature/n1-login-google-oauth
feature/n2-create-event
feature/n4-orchestrator-agent
fix/n3-weather-api-timeout
hotfix/jwt-refresh-token-expiry
refactor/n2-plan-service
docs/update-api-design-guide
test/n4-conflict-resolver-agent
```

## Ví dụ sai
```
new-feature          ❌ thiếu type, không rõ nội dung
Feature/Login         ❌ viết hoa, thiếu mô tả
fix-bug                ❌ thiếu dấu "/", quá chung chung
minh-dev-branch        ❌ đặt theo tên người, không theo nội dung
```

> Không tạo branch đặt theo tên riêng của từng người (VD `minh-dev`). Branch phản ánh **công việc**, không phải **người làm**, để dễ tái sử dụng/tiếp quản khi cần.
