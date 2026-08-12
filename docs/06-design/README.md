# 🎨 Design Docs — UI/UX (Sprint 0)

> Đây là **nguồn chân lý thiết kế (single source of truth)** cho toàn bộ giao diện.
> Được tạo ở **Sprint 0** song song với Contract Session, làm trước khi FE Dev A & B bắt đầu code.
> Mọi màn hình ở Sprint 1–4 phải bám theo bộ tài liệu này; đổi thiết kế giữa chừng → theo quy trình Contract Change ([contract-first-workflow.md](../01-workflow/contract-first-workflow.md)).

## Quy trình làm việc (Design → Code)

```
TASK-009 (Design Tokens) ──► TASK-111 (Project Skeleton & Design System) ──► mọi màn hình
TASK-010 (User Flows & Wireframes) ──► layout/component từng page (Sprint 1–4)
TASK-011 (Hi-fi Mockups + Component Library + A11y) ──► Figma cho FE dev & review
```

- **FE Dev A** (TASK-009): định nghĩa design tokens → áp vào Tailwind/shadcn config.
- **FE Dev B** (TASK-010, 011): vẽ wireframe + hi-fi mockup → chuyển cho cả team làm theo.
- Đối chiếu lại **trước Integration Day** cuối mỗi Sprint để tránh lệch pixel với hiện thực.

## Cấu trúc thư mục

```
docs/06-design/
├── README.md            ← File này: overview + quy trình
├── design-tokens.md     ← Palette (light/dark), typography, spacing, radius, shadow (TASK-009)
├── user-flows.md        ← Flowchart các luồng chính bằng Mermaid/ASCII (TASK-010)
├── wireframes/          ← Wireframe từng page: layout + component + empty/loading/error state (TASK-010)
└── mockups.md           ← Link hi-fi mockups trên Figma + ghi chú responsive/a11y (TASK-011)
```

## Các luồng phải cover (User Flows)

1. Register/Login (kèm OAuth2) → Event Dashboard
2. Tạo event (6 `EventType`) → Mời member (Invitation)
3. Tạo plan thủ công / AI gợi ý → Vote → Confirm
4. AI Chat streaming (tạo/hỏi điều chỉnh plan)
5. Chia chi phí: Fund pool → Expense → Settlement tối ưu
6. Admin Dashboard (token usage, user management)

## Nguyên tắc thiết kế bắt buộc

- **Design Tokens trước, component sau**: không hardcode màu/typography lẻ tẻ trong component.
- **Mỗi component đủ states**: default / hover / disabled / loading / empty / error.
- **Responsive**: mobile-first, breakpoint chuẩn Tailwind (sm/md/lg/xl).
- **Accessibility (WCAG AA)**: contrast ≥ 4.5:1 cho text, focus visible, label cho form control.
- **i18n sẵn sàng**: text UI đi qua `react-i18next` (vi/en), mockup ghi rõ chỗ text động.

## Task liên quan

| Task | Chủ sở hữu | Output |
|---|---|---|
| [TASK-009](../TASKS.md) | FE Dev A | `design-tokens.md` + theme config |
| [TASK-010](../TASKS.md) | FE Dev B | `user-flows.md` + `wireframes/` |
| [TASK-011](../TASKS.md) | FE Dev B | `mockups.md` + component variants + a11y |
