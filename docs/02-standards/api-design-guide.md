# API Design Guide

## 1. Nguyên tắc REST
- Resource là **danh từ số nhiều**, không dùng động từ trong URL.
- Dùng đúng HTTP method để thể hiện hành động:

| Method | Ý nghĩa | Ví dụ |
|---|---|---|
| `GET` | Đọc dữ liệu | `GET /events`, `GET /events/:id` |
| `POST` | Tạo mới | `POST /events` |
| `PATCH` | Cập nhật 1 phần | `PATCH /events/:id` |
| `PUT` | Thay thế toàn bộ (ít dùng) | — |
| `DELETE` | Xoá | `DELETE /events/:id` |

## 2. Versioning
- Prefix version ở đầu path: `/api/v1/...`
- Khi có breaking change ở endpoint đang được dùng → tạo `v2`, không sửa thẳng `v1` (tránh phá vỡ FE/Agent khác đang gọi).

## 3. Cấu trúc endpoint theo nhóm tính năng

```
/api/v1/auth
  POST   /auth/login/google
  POST   /auth/login/facebook
  POST   /auth/register
  POST   /auth/forgot-password
  POST   /auth/refresh-token
  GET    /auth/me

/api/v1/users
  GET    /users/:id/profile
  PATCH  /users/:id/profile

/api/v1/events
  GET    /events                                       # lấy danh sách event của user
  POST   /events                                       # tạo event (name, type: EventType, location, dates)
  GET    /events/:id                                   # chi tiết event + thành viên + plans
  PATCH  /events/:id                                   # sửa thông tin event
  DELETE /events/:id                                   # xoá event (chỉ Owner)
  GET    /events/:id/members                           # lấy danh sách thành viên

/api/v1/invitations
  POST   /events/:eventId/invitations                  # gửi lời mời vào event (email / userId)
  GET    /invitations/me                               # danh sách lời mời của user hiện tại
  PATCH  /invitations/:id                              # chấp nhận (ACCEPTED) hoặc từ chối (DECLINED)

/api/v1/events/:eventId/plans
  GET    /events/:eventId/plans                        # danh sách plans trong event
  POST   /events/:eventId/plans                        # tạo plan mới (AI hoặc thủ công, isAiGenerated: bool)
  GET    /events/:eventId/plans/:planId                # chi tiết plan + stops + votes
  PATCH  /events/:eventId/plans/:planId                # sửa thông tin plan (title, budget...)
  PATCH  /events/:eventId/plans/:planId/status         # chuyển trạng thái: DRAFT -> VOTING -> CONFIRMED
  DELETE /events/:eventId/plans/:planId                # xoá plan
  PATCH  /events/:eventId/plans/:planId/stops          # đổi thứ tự / thêm / xoá / sửa điểm dừng (PlanStop)

/api/v1/events/:eventId/plans/:planId/votes
  POST   /events/:eventId/plans/:planId/votes          # vote UP / DOWN / NEUTRAL + comment
  GET    /events/:eventId/plans/:planId/votes          # xem danh sách và kết quả vote

/api/v1/places        (Nhóm 3)
  GET    /places/search?keyword=&lat=&lng=&category=   # tra cứu địa điểm, category: RESTAURANT, CAFE, ENTERTAINMENT, ATTRACTION, HOTEL
  GET    /hotels/compare?ids=                          # so sánh khách sạn

/api/v1/utils          (Nhóm 3)
  GET    /weather?lat=&lng=
  GET    /exchange-rate?from=&to=

/api/v1/ai              (Nhóm 4)
  POST   /ai/orchestrator/run          # điểm vào chính, orchestrator tự điều phối sub-agent theo EventType
  POST   /ai/chat                       # màn hình chat với AI (15)
  GET    /ai/chat/:sessionId/history
  POST   /ai/agents/booking/suggest
  POST   /ai/agents/location/search
  POST   /ai/agents/plan/generate
  POST   /ai/agents/research
  POST   /ai/agents/conflict-resolver
  POST   /ai/agents/cost-estimator

/api/v1/notifications    (Nhóm 5)
  GET    /notifications
  POST   /notifications/mark-read

/api/v1/export            (Nhóm 5)
  GET    /events/:eventId/export/pdf

/api/v1/admin               (Nhóm 6)
  GET    /admin/users
  GET    /admin/usage/tokens
  GET    /admin/dashboard/overview
```

## 4. Response format chuẩn (dùng chung toàn hệ thống)
```jsonc
// Thành công
{
  "success": true,
  "data": { /* payload */ },
  "meta": { "page": 1, "limit": 20, "total": 57 }   // chỉ khi có phân trang
}

// Lỗi
{
  "success": false,
  "error": {
    "code": "EVENT_NOT_FOUND",
    "message": "Không tìm thấy event",
    "details": null
  }
}
```
- `error.code` dùng `UPPER_SNAKE_CASE`, thống nhất danh sách trong `common/exceptions/error-codes.ts` — tránh mỗi người tự đặt 1 kiểu.

## 5. HTTP status code chuẩn
| Code | Khi nào dùng |
|---|---|
| `200` | Thành công (GET, PATCH, DELETE) |
| `201` | Tạo mới thành công (POST) |
| `400` | Input sai/validate fail |
| `401` | Chưa đăng nhập / token hết hạn |
| `403` | Đã đăng nhập nhưng không đủ quyền (VD Viewer cố sửa plan) |
| `404` | Không tìm thấy resource |
| `409` | Xung đột (VD vote trùng) |
| `422` | Input đúng format nhưng sai logic nghiệp vụ |
| `429` | Rate limit (quan trọng cho endpoint AI Agent & external API) |
| `500` | Lỗi server không mong muốn |

## 6. Domain & Subdomain (khi deploy)
| Service | Domain gợi ý |
|---|---|
| Frontend | `travel-ai.<domain>.com` hoặc domain chính |
| Backend API | `api.travel-ai.<domain>.com` |
| AI Service (nếu tách riêng Python) | `ai.travel-ai.<domain>.com` |
| Admin Dashboard | `admin.travel-ai.<domain>.com` (hoặc route `/admin` trong FE chính nếu không tách) |

## 7. Rate limiting
- Áp dụng rate limit riêng cho nhóm endpoint `/ai/*` (chi phí LLM cao) — VD tối đa 20 request/phút/user.
- Áp dụng rate limit cho `/places/*`, `/weather`, `/exchange-rate` để tránh vượt quota free-tier của API bên thứ 3 (kết hợp cache Redis, xem `03-architecture`).

## 8. Tài liệu API tự động
- Dùng **Swagger/OpenAPI** (`@nestjs/swagger`) sinh doc tự động từ decorator trong code — tránh viết doc API thủ công dễ lệch với code thật. Truy cập `/api/docs` ở môi trường dev.
