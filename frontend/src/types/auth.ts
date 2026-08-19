/**
 * TypeScript interfaces for Auth & User APIs.
 * Mirrors backend Pydantic schemas: schemas/user.py
 * Endpoints: api-design-guide.md Section 3 — /api/v1/auth, /api/v1/users
 */

// --- Enums ---
export type SystemRole = 'USER' | 'ADMIN';
export type AuthProvider = 'LOCAL' | 'GOOGLE' | 'FACEBOOK';

// --- Requests ---
export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  email: string;
  full_name: string;
  password: string;
}

// --- Responses ---
export interface TokenResponse {
  access_token: string;
  token_type: 'bearer';
}

export interface UserResponse {
  id: string;
  email: string;
  full_name: string;
  avatar_url: string | null;
  provider: AuthProvider;
  role: SystemRole;
  created_at: string; // ISO 8601
}
