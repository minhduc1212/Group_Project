import { http, HttpResponse } from 'msw';
import type {
  PlanResponse,
  PlanStopResponse,
  PlanVoteResponse,
  PlanStatus,
  VoteValue,
} from '../../types/plan';
import type { ApiResponse, ApiErrorResponse } from '../../types/api';

/**
 * MSW Mock Handlers for Plan, PlanStop & Vote APIs.
 * Endpoints follow api-design-guide.md Section 3.
 * Response format follows api-design-guide.md Section 4.
 */

const mockStops: PlanStopResponse[] = [
  {
    id: 'stop_001',
    plan_id: 'plan_001',
    order: 1,
    place_name: 'Hồ Xuân Hương',
    place_ref_id: 'ChIJxyz123',
    lat: 11.9465,
    lng: 108.4419,
    note: 'Đến sáng sớm để chụp hình đẹp',
    estimated_cost: '0',
    category: 'ATTRACTION',
    start_time: '2024-12-20T07:00:00Z',
    duration_minutes: 60,
    metadata: null,
  },
  {
    id: 'stop_002',
    plan_id: 'plan_001',
    order: 2,
    place_name: 'Quán Bún Bò Huế Bà Hồng',
    place_ref_id: 'ChIJabc456',
    lat: 11.9404,
    lng: 108.4383,
    note: 'Ăn sáng nổi tiếng',
    estimated_cost: '50000',
    category: 'RESTAURANT',
    start_time: '2024-12-20T08:30:00Z',
    duration_minutes: 45,
    metadata: null,
  },
  {
    id: 'stop_003',
    plan_id: 'plan_001',
    order: 3,
    place_name: 'Dinh Bảo Đại',
    place_ref_id: 'ChIJdef789',
    lat: 11.9335,
    lng: 108.4267,
    note: 'Tham quan dinh thự lịch sử',
    estimated_cost: '100000',
    category: 'ATTRACTION',
    start_time: '2024-12-20T10:00:00Z',
    duration_minutes: 90,
    metadata: null,
  },
];

let mockPlans: PlanResponse[] = [
  {
    id: 'plan_001',
    event_id: 'evt_001',
    title: 'Lịch trình Đà Lạt 3 ngày 2 đêm',
    total_budget: '3000000',
    status: 'DRAFT',
    is_ai_generated: false,
    created_by_id: 'usr_001',
    created_at: '2024-12-05T10:00:00Z',
    stops: mockStops,
  },
  {
    id: 'plan_002',
    event_id: 'evt_001',
    title: 'AI gợi ý: Tour Đà Lạt tiết kiệm',
    total_budget: '2000000',
    status: 'VOTING',
    is_ai_generated: true,
    created_by_id: null,
    created_at: '2024-12-06T14:00:00Z',
    stops: [],
  },
];

let mockVotes: PlanVoteResponse[] = [
  {
    id: 'vote_001',
    plan_id: 'plan_002',
    user_id: 'usr_001',
    value: 'UP',
    comment: 'Lịch trình hợp lý, ngân sách tiết kiệm!',
    created_at: '2024-12-07T09:00:00Z',
  },
  {
    id: 'vote_002',
    plan_id: 'plan_002',
    user_id: 'usr_002',
    value: 'DOWN',
    comment: 'Thiếu quán cà phê view đẹp',
    created_at: '2024-12-07T10:30:00Z',
  },
];

export const planHandlers = [
  // GET /api/v1/events/:eventId/plans
  http.get('/api/v1/events/:eventId/plans', ({ params }) => {
    const plans = mockPlans.filter((p) => p.event_id === params.eventId);

    return HttpResponse.json(
      { success: true, data: plans },
      { status: 200 },
    );
  }),

  // POST /api/v1/events/:eventId/plans
  http.post('/api/v1/events/:eventId/plans', async ({ params, request }) => {
    const body = (await request.json()) as {
      title: string;
      total_budget?: string;
      is_ai_generated?: boolean;
    };

    const newPlan: PlanResponse = {
      id: `plan_${Date.now()}`,
      event_id: params.eventId as string,
      title: body.title,
      total_budget: body.total_budget ?? null,
      status: 'DRAFT',
      is_ai_generated: body.is_ai_generated ?? false,
      created_by_id: 'usr_001',
      created_at: new Date().toISOString(),
      stops: [],
    };

    mockPlans.push(newPlan);

    return HttpResponse.json(
      { success: true, data: newPlan },
      { status: 201 },
    );
  }),

  // GET /api/v1/events/:eventId/plans/:planId
  http.get('/api/v1/events/:eventId/plans/:planId', ({ params }) => {
    const plan = mockPlans.find((p) => p.id === params.planId);

    if (!plan) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'PLAN_NOT_FOUND', message: 'Không tìm thấy plan', details: null },
        },
        { status: 404 },
      );
    }

    return HttpResponse.json(
      { success: true, data: plan },
      { status: 200 },
    );
  }),

  // PATCH /api/v1/events/:eventId/plans/:planId
  http.patch('/api/v1/events/:eventId/plans/:planId', async ({ params, request }) => {
    const idx = mockPlans.findIndex((p) => p.id === params.planId);

    if (idx === -1) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'PLAN_NOT_FOUND', message: 'Không tìm thấy plan', details: null },
        },
        { status: 404 },
      );
    }

    const body = (await request.json()) as Partial<Pick<PlanResponse, 'title' | 'total_budget'>>;
    mockPlans[idx] = { ...mockPlans[idx], ...body };

    return HttpResponse.json(
      { success: true, data: mockPlans[idx] },
      { status: 200 },
    );
  }),

  // PATCH /api/v1/events/:eventId/plans/:planId/status
  http.patch('/api/v1/events/:eventId/plans/:planId/status', async ({ params, request }) => {
    const idx = mockPlans.findIndex((p) => p.id === params.planId);

    if (idx === -1) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'PLAN_NOT_FOUND', message: 'Không tìm thấy plan', details: null },
        },
        { status: 404 },
      );
    }

    const body = (await request.json()) as { status: PlanStatus };
    mockPlans[idx] = { ...mockPlans[idx], status: body.status };

    return HttpResponse.json(
      { success: true, data: mockPlans[idx] },
      { status: 200 },
    );
  }),

  // DELETE /api/v1/events/:eventId/plans/:planId
  http.delete('/api/v1/events/:eventId/plans/:planId', ({ params }) => {
    const idx = mockPlans.findIndex((p) => p.id === params.planId);

    if (idx === -1) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'PLAN_NOT_FOUND', message: 'Không tìm thấy plan', details: null },
        },
        { status: 404 },
      );
    }

    mockPlans = mockPlans.filter((p) => p.id !== params.planId);

    return HttpResponse.json(
      { success: true, data: null },
      { status: 200 },
    );
  }),

  // PATCH /api/v1/events/:eventId/plans/:planId/stops
  http.patch('/api/v1/events/:eventId/plans/:planId/stops', async ({ params, request }) => {
    const idx = mockPlans.findIndex((p) => p.id === params.planId);

    if (idx === -1) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'PLAN_NOT_FOUND', message: 'Không tìm thấy plan', details: null },
        },
        { status: 404 },
      );
    }

    const body = (await request.json()) as { stops: PlanStopResponse[] };
    mockPlans[idx] = { ...mockPlans[idx], stops: body.stops };

    return HttpResponse.json(
      { success: true, data: mockPlans[idx] },
      { status: 200 },
    );
  }),

  // POST /api/v1/events/:eventId/plans/:planId/votes
  http.post('/api/v1/events/:eventId/plans/:planId/votes', async ({ params, request }) => {
    const body = (await request.json()) as { value: VoteValue; comment?: string };

    const newVote: PlanVoteResponse = {
      id: `vote_${Date.now()}`,
      plan_id: params.planId as string,
      user_id: 'usr_001',
      value: body.value,
      comment: body.comment ?? null,
      created_at: new Date().toISOString(),
    };

    mockVotes.push(newVote);

    return HttpResponse.json(
      { success: true, data: newVote },
      { status: 201 },
    );
  }),

  // GET /api/v1/events/:eventId/plans/:planId/votes
  http.get('/api/v1/events/:eventId/plans/:planId/votes', ({ params }) => {
    const votes = mockVotes.filter((v) => v.plan_id === params.planId);

    return HttpResponse.json(
      { success: true, data: votes },
      { status: 200 },
    );
  }),
];
