/**
 * Standard API response wrapper.
 * Follows api-design-guide.md Section 4.
 */

export interface ApiResponse<T> {
  success: true;
  data: T;
  meta?: {
    page: number;
    limit: number;
    total: number;
  };
}

export interface ApiErrorResponse {
  success: false;
  error: {
    code: string;
    message: string;
    details: unknown | null;
  };
}
