/**
 * TypeScript interfaces for Plan, PlanStop & Vote APIs.
 * Mirrors backend Pydantic schemas: schemas/plan.py, schemas/vote.py
 * Endpoints: api-design-guide.md Section 3 — /api/v1/events/{eventId}/plans, votes
 */

// --- Enums ---
export type PlanStatus = 'DRAFT' | 'VOTING' | 'CONFIRMED' | 'ARCHIVED';

export type StopCategory =
  | 'ATTRACTION'
  | 'RESTAURANT'
  | 'CAFE'
  | 'HOTEL'
  | 'ENTERTAINMENT'
  | 'TRANSPORT'
  | 'SHOPPING'
  | 'OTHER';

export type VoteValue = 'UP' | 'DOWN' | 'NEUTRAL';

// --- Requests ---
export interface PlanCreateRequest {
  title: string;
  total_budget?: string | null;
  is_ai_generated?: boolean;
}

export interface PlanVoteCreateRequest {
  value: VoteValue;
  comment?: string | null;
}

// --- Plan Stop Response ---
export interface PlanStopResponse {
  id: string;
  plan_id: string;
  order: number;
  place_name: string;
  place_ref_id: string | null;
  lat: number | null;
  lng: number | null;
  note: string | null;
  estimated_cost: string | null; // Decimal serialized as string
  category: StopCategory | null;
  start_time: string | null;
  duration_minutes: number | null;
  metadata: Record<string, unknown> | null;
}

// --- Plan Response ---
export interface PlanResponse {
  id: string;
  event_id: string;
  title: string;
  total_budget: string | null; // Decimal serialized as string
  status: PlanStatus;
  is_ai_generated: boolean;
  created_by_id: string | null;
  created_at: string;
  stops: PlanStopResponse[];
}

// --- Vote Response ---
export interface PlanVoteResponse {
  id: string;
  plan_id: string;
  user_id: string;
  value: VoteValue;
  comment: string | null;
  created_at: string;
}
