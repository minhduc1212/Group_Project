from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.enums import VoteValue

class PlanVoteBase(BaseModel):
    value: VoteValue
    comment: Optional[str] = None

class PlanVoteCreate(PlanVoteBase):
    pass

class PlanVoteResponse(PlanVoteBase):
    id: str
    plan_id: str
    user_id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
