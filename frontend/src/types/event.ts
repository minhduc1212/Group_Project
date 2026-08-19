/**
 * TypeScript interfaces for Event & Invitation APIs.
 * Mirrors backend Pydantic schemas: schemas/event.py, schemas/invitation.py
 * Endpoints: api-design-guide.md Section 3 — /api/v1/events, /api/v1/invitations
 */

// --- Enums ---
export type EventType =
  | 'TRAVEL'
  | 'DINING'
  | 'HANGOUT'
  | 'ENTERTAINMENT'
  | 'SIGHTSEEING'
  | 'CUSTOM';

export type EventRole = 'OWNER' | 'MEMBER' | 'VIEWER';

export type InvitationStatus = 'PENDING' | 'ACCEPTED' | 'DECLINED' | 'EXPIRED';

// --- Requests ---
export interface EventCreateRequest {
  name: string;
  description?: string | null;
  type?: EventType;
  location?: string | null;
  start_date: string; // ISO 8601
  end_date: string;
}

// --- Responses ---
export interface EventResponse {
  id: string;
  name: string;
  description: string | null;
  type: EventType;
  location: string | null;
  start_date: string;
  end_date: string;
  created_at: string;
}

export interface EventMemberResponse {
  id: string;
  event_id: string;
  user_id: string;
  role: EventRole;
}

export interface InvitationResponse {
  id: string;
  event_id: string;
  email: string | null;
  invited_by: string;
  invited_user_id: string | null;
  status: InvitationStatus;
  created_at: string;
  expires_at: string | null;
}
