import { http, HttpResponse } from 'msw';
import type { TokenResponse, UserResponse, RegisterRequest } from '../../types/auth';
import type { ApiResponse, ApiErrorResponse } from '../../types/api';

/**
 * MSW Mock Handlers for Auth & User APIs.
 * Endpoints follow api-design-guide.md Section 3.
 * Response format follows api-design-guide.md Section 4.
 */

let mockUser: UserResponse = {
  id: 'usr_001',
  email: 'hadanghuy@example.com',
  full_name: 'Hà Đăng Huy',
  avatar_url: null,
  provider: 'LOCAL',
  role: 'USER',
  created_at: '2024-12-01T08:00:00Z',
};

export const authHandlers = [
  // POST /api/v1/auth/login/google
  http.post('/api/v1/auth/login/google', () => {
    return HttpResponse.json<ApiResponse<TokenResponse>>(
      {
        success: true,
        data: { access_token: 'mock-google-jwt-token', token_type: 'bearer' },
      },
      { status: 200 },
    );
  }),

  // POST /api/v1/auth/login/facebook
  http.post('/api/v1/auth/login/facebook', () => {
    return HttpResponse.json<ApiResponse<TokenResponse>>(
      {
        success: true,
        data: { access_token: 'mock-facebook-jwt-token', token_type: 'bearer' },
      },
      { status: 200 },
    );
  }),

  // POST /api/v1/auth/register
  http.post('/api/v1/auth/register', async ({ request }) => {
    const body = (await request.json()) as RegisterRequest;

    return HttpResponse.json<ApiResponse<TokenResponse>>(
      {
        success: true,
        data: { access_token: `mock-jwt-for-${body.email}`, token_type: 'bearer' },
      },
      { status: 201 },
    );
  }),

  // POST /api/v1/auth/forgot-password
  http.post('/api/v1/auth/forgot-password', () => {
    return HttpResponse.json<ApiResponse<{ message: string }>>(
      {
        success: true,
        data: { message: 'Password reset link sent' },
      },
      { status: 200 },
    );
  }),

  // POST /api/v1/auth/refresh-token
  http.post('/api/v1/auth/refresh-token', () => {
    return HttpResponse.json<ApiResponse<TokenResponse>>(
      {
        success: true,
        data: { access_token: 'mock-jwt-refreshed-token', token_type: 'bearer' },
      },
      { status: 200 },
    );
  }),

  // GET /api/v1/users/me
  http.get('/api/v1/users/me', ({ request }) => {
    const authHeader = request.headers.get('Authorization');

    if (!authHeader) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'UNAUTHORIZED', message: 'Chưa đăng nhập', details: null },
        },
        { status: 401 },
      );
    }

    return HttpResponse.json(
      { success: true, data: mockUser },
      { status: 200 },
    );
  }),

  // PATCH /api/v1/users/me
  http.patch('/api/v1/users/me', async ({ request }) => {
    const authHeader = request.headers.get('Authorization');

    if (!authHeader) {
      return HttpResponse.json(
        {
          success: false,
          error: { code: 'UNAUTHORIZED', message: 'Chưa đăng nhập', details: null },
        },
        { status: 401 },
      );
    }

    const body = (await request.json()) as Partial<Pick<UserResponse, 'full_name' | 'avatar_url'>>;
    mockUser = { ...mockUser, ...body };

    return HttpResponse.json(
      { success: true, data: mockUser },
      { status: 200 },
    );
  }),
];
