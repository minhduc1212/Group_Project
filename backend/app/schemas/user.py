from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional
from datetime import datetime
from app.models.enums import SystemRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    avatar_url: Optional[str] = None
    role: SystemRole = SystemRole.USER

class UserCreate(UserBase):
    # Added strict length requirements
    password: str = Field(..., min_length=8, max_length=128, description="Password must be 8-128 characters")

class UserResponse(UserBase):
    id: str
    provider: str
    created_at: datetime
    role: SystemRole
    model_config = ConfigDict(from_attributes=True)
