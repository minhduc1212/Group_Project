from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime
from app.models.enums import SystemRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    avatar_url: Optional[str] = None
    role: SystemRole = SystemRole.USER

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str
    provider: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
