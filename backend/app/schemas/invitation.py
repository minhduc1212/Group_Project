from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime
from app.models.enums import InvitationStatus

class InvitationBase(BaseModel):
    email: Optional[EmailStr] = None

class InvitationCreate(InvitationBase):
    invited_user_id: Optional[str] = None

class InvitationResponse(InvitationBase):
    id: str
    event_id: str
    invited_by: str
    invited_user_id: Optional[str]
    status: InvitationStatus
    created_at: datetime
    expires_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
