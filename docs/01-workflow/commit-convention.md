# Commit Message Convention

Team áp dụng chuẩn **[Conventional Commits](https://www.conventionalcommits.org/)** — giúp tự động sinh changelog và dễ tra cứu lịch sử.

## Format
```
<type>(<scope>): <mô tả ngắn, thì hiện tại, không viết hoa đầu câu, không dấu chấm cuối>

[phần thân - tuỳ chọn, giải thích "tại sao" chứ không chỉ "cái gì"]

[footer - tuỳ chọn: BREAKING CHANGE, Closes #issue]
```

## Các `type`
| Type | Ý nghĩa |
|---|---|
| `feat` | Thêm tính năng mới |
| `fix` | Sửa lỗi |
| `refactor` | Tái cấu trúc, không đổi hành vi/tính năng |
| `perf` | Cải thiện hiệu năng |
| `test` | Thêm/sửa test |
| `docs` | Chỉ thay đổi tài liệu |
| `style` | Format code (dấu cách, dấu chấm phẩy...), không đổi logic |
| `chore` | Cập nhật dependency, cấu hình build, CI |
| `revert` | Revert lại 1 commit trước đó |

## `scope` gợi ý (theo module/nhóm tính năng)
`auth`, `event`, `plan`, `vote`, `agent-orchestrator`, `agent-booking`, `agent-plan`, `agent-cost`, `map`, `weather`, `notification`, `export`, `admin`, `i18n`, `security`

## Ví dụ đúng
```
feat(auth): thêm đăng nhập qua Google OAuth2

fix(agent-cost): sửa lỗi tính sai chi phí khi vote thay đổi số người

refactor(plan): tách logic tính plan ra khỏi controller

docs(api-design): cập nhật endpoint tạo event

test(agent-orchestrator): thêm test cho luồng phân giải xung đột vote

chore(deps): nâng cấp langgraph lên v0.4

feat(auth)!: đổi cấu trúc JWT payload

BREAKING CHANGE: field `userId` trong JWT đổi thành `sub`, cần cập nhật middleware verify token ở FE.
Closes #42
```

## Ví dụ sai
```
update code                ❌ không có type, không rõ nội dung
Fixed bug.                 ❌ viết hoa, có dấu chấm, không theo format
"sửa lỗi login"             ❌ không dùng type tiếng Anh chuẩn, khó tự động parse
asdasd                      ❌ vô nghĩa
```

## Quy tắc bổ sung
- 1 commit nên là 1 thay đổi logic hoàn chỉnh, có thể build/test được (tránh commit "wip" tràn lan trên branch chung; commit nháp chỉ nên tồn tại trên branch cá nhân, squash lại trước khi merge).
- Dùng `!` sau type hoặc footer `BREAKING CHANGE:` khi thay đổi phá vỡ tương thích (đổi API contract, đổi schema DB).
- Tham chiếu Issue bằng `Closes #<số>` / `Refs #<số>` trong footer khi có.
