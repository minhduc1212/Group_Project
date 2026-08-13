from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String , Enum
from typing import List, Optional
from .enums import SystemRole

class User(Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String)
    avatar_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    provider: Mapped[str] = mapped_column(String, default="LOCAL")
    role: Mapped[SystemRole] = mapped_column(Enum(SystemRole), default=SystemRole.USER) 
    
    event_members: Mapped[List["EventMember"]] = relationship("EventMember",back_populates="user")
  