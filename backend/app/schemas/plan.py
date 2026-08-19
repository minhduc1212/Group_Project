from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, Dict
from datetime import datetime
from app.models.enums import PlanStatus, StopCategory

# --- Plan ---
class PlanBase(BaseModel):
    title: str
    total_budget: Optional[float] = None

class PlanCreate(PlanBase):
    is_ai_generated: bool = False

class PlanResponse(PlanBase):
    id: str
    event_id: str
    status: PlanStatus
    is_ai_generated: bool
    created_by_id: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# --- PlanStop ---
class PlanStopBase(BaseModel):
    order: int
    place_name: str
    place_ref_id: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    note: Optional[str] = None
    estimated_cost: Optional[float] = None
    category: Optional[StopCategory] = None
    start_time: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    metadata_: Optional[Dict[str, Any]] = None

class PlanStopCreate(PlanStopBase):
    pass

class PlanStopResponse(PlanStopBase):
    id: str
    plan_id: str

    model_config = ConfigDict(from_attributes=True)
