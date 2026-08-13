from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.enums import EventType, EventRole

class EventBase(BaseModel):
    name: str
    description: Optional[str] = None
    type: EventType = EventType.TRAVEL
    location: Optional[str] = None
    start_date: datetime
    end_date: datetime

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EventMemberResponse(BaseModel):
    id: str
    event_id: str
    user_id: str
    role: EventRole
    
    model_config = ConfigDict(from_attributes=True)