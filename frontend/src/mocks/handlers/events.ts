import { http, HttpResponse } from 'msw';
import type { EventResponse, EventCreateRequest, EventMemberResponse, InvitationResponse } from '../../types/event';
import type { ApiResponse, ApiErrorResponse } from '../../types/api';

/**
 * MSW Mock Handlers for Event & Invitation APIs.
 * Endpoints follow api-design-guide.md Section 3.
 * Response format follows api-design-guide.md Section 4.
 */

let mockEvents: EventResponse[] = [
  {
    id: 'evt_001',
    name: 'Chuyến đi Đà Lạt',
    description: 'Du lịch nhóm cuối tuần tại Đà Lạt',
    type: 'TRAVEL',
    location: 'Đà Lạt, Lâm Đồng',
    start_date: '2024-12-20T08:00:00Z',
    end_date: '2024-12-22T20:00:00Z',
    created_at: '2024-12-01T10:00:00Z',
  },
  {
    id: 'evt_002',
    name: 'Ăn lẩu team building',
    description: 'Team building quý 4',
    type: 'DINING',
    location: 'Quận 1, TP.HCM',
    start_date: '2024-12-15T18:00:00Z',
    end_date: '2024-12-15T22:00:00Z',
    created_at: '2024-12-05T09:00:00Z',
  },
];

const mockMembers: EventMemberResponse[] = [
  { id: 'mem_001', event_id: 'evt_001', user_id: 'usr_001', role: 'OWNER' },
  { id: 'mem_002', event_id: 'evt_001', user_id: 'usr_002', role: 'MEMBER' },
  { id: 'mem_003', event_id: 'evt_001', user_id: 'usr_003', role: 'MEMBER' },
];

export const eventHandlers = [
  // GET /api/v1/events
  http.get('/api/v1/events', () => {
    return HttpResponse.json(
      { success: true, data: mockEvents },
      { status: 200 },
    );
  }),

  // POST /api/v1/events
  http.post('/api/v1/events', async ({ request }) => {
    const body = (await request.json()) as EventCreateRequest;

    const newEvent: EventResponse = {
      id: `evt_${Date.now()}`,
      name: body.name,
      description: body.description ?? null,
      type: body.type ?? 'TRAVEL',
      location: body.location ?? null,
      start_date: body.start_date,
      end_date: body.end_date,
      created_at: new Date().toISOString(),
    };

    mockEvents.push(newEvent);

    return HttpResponse.json(
      { success: true, data: newEvent },
      { status: 201 },
    );
  }),

  // GET /api/v1/events/:eventId
  http.get('/api/v1/events/:eventId', ({ params }) => {
    const event = mockEvents.find((e) => e.id === params.eventId);

    if (!event) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'EVENT_NOT_FOUND', message: 'Không tìm thấy event', details: null },
        },
        { status: 404 },
      );
    }

    return HttpResponse.json(
      { success: true, data: event },
      { status: 200 },
    );
  }),

  // PATCH /api/v1/events/:eventId
  http.patch('/api/v1/events/:eventId', async ({ params, request }) => {
    const idx = mockEvents.findIndex((e) => e.id === params.eventId);

    if (idx === -1) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'EVENT_NOT_FOUND', message: 'Không tìm thấy event', details: null },
        },
        { status: 404 },
      );
    }

    const body = (await request.json()) as Partial<EventCreateRequest>;
    mockEvents[idx] = { ...mockEvents[idx], ...body };

    return HttpResponse.json(
      { success: true, data: mockEvents[idx] },
      { status: 200 },
    );
  }),

  // DELETE /api/v1/events/:eventId
  http.delete('/api/v1/events/:eventId', ({ params }) => {
    const idx = mockEvents.findIndex((e) => e.id === params.eventId);

    if (idx === -1) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'EVENT_NOT_FOUND', message: 'Không tìm thấy event', details: null },
        },
        { status: 404 },
      );
    }

    mockEvents = mockEvents.filter((e) => e.id !== params.eventId);

    return HttpResponse.json(
      { success: true, data: null },
      { status: 200 },
    );
  }),

  // GET /api/v1/events/:eventId/members
  http.get('/api/v1/events/:eventId/members', ({ params }) => {
    const members = mockMembers.filter((m) => m.event_id === params.eventId);

    return HttpResponse.json(
      { success: true, data: members },
      { status: 200 },
    );
  }),

  // POST /api/v1/events/:eventId/invitations
  http.post('/api/v1/events/:eventId/invitations', async ({ params, request }) => {
    const body = (await request.json()) as { email?: string; invited_user_id?: string };

    const newInvitation: InvitationResponse = {
      id: `inv_${Date.now()}`,
      event_id: params.eventId as string,
      email: body.email ?? null,
      invited_by: 'usr_001',
      invited_user_id: body.invited_user_id ?? null,
      status: 'PENDING',
      created_at: new Date().toISOString(),
      expires_at: null,
    };

    return HttpResponse.json(
      { success: true, data: newInvitation },
      { status: 201 },
    );
  }),

  // GET /api/v1/invitations/me
  http.get('/api/v1/invitations/me', () => {
    return HttpResponse.json(
      { success: true, data: [] },
      { status: 200 },
    );
  }),

  // PATCH /api/v1/invitations/:id
  http.patch('/api/v1/invitations/:id', async ({ params, request }) => {
    const body = (await request.json()) as { status: 'ACCEPTED' | 'DECLINED' };

    return HttpResponse.json(
      {
        success: true,
        data: { id: params.id as string, status: body.status },
      },
      { status: 200 },
    );
  }),
];
