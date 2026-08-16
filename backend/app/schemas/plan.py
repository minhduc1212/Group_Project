from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Any, Dict
from datetime import datetime
from app.models.enums import PlanStatus, StopCategory
from decimal import Decimal
# --- Plan ---
class PlanBase(BaseModel):
    title: str
    total_budget: Optional[Decimal] = Field(None, ge=0)

class PlanCreate(PlanBase):
    is_ai_generated: bool = False

class PlanResponse(PlanBase):
    id: str
    event_id: str
    status: PlanStatus
    is_ai_generated: bool
    created_by_id: Optional[str]
    created_at: datetime

    # URGENT: Added nested stops so the frontend can render the timeline
    stops: list[PlanStopResponse] = []

    model_config = ConfigDict(from_attributes=True)

# --- PlanStop ---
class PlanStopBase(BaseModel):
    order: int
    place_name: str
    place_ref_id: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    note: Optional[str] = None
    
    # URGENT: Changed to Decimal
    estimated_cost: Optional[Decimal] = Field(None, ge=0)

    category: Optional[StopCategory] = None
    start_time: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    
    metadata_: Optional[Dict[str, Any]] = None
    

    # URGENT: Re-maps the frontend 'metadata' to the backend 'metadata_'
    metadata_: Optional[Dict[str, Any]] = Field(None, alias="metadata")

class PlanStopCreate(PlanStopBase):
    pass

class PlanStopResponse(PlanStopBase):
    id: str
    plan_id: str

    model_config = ConfigDict(from_attributes=True)
