from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey, UniqueConstraint, DateTime
from typing import List, Optional
from datetime import datetime
from backend.app.models.user import User
from .base import Base
from .enums import EventType, EventRole

class Event(Base):
    __tablename__ = "events"

    name: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String, nullable= True)
    type: Mapped[EventType] = mapped_column(Enum(EventType), default=EventType.TRAVEL)
    location: Mapped[Optional[str]] = mapped_column(String, nullable = True)
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime] = mapped_column(DateTime)

    members: Mapped[List["EventMember"]] = relationship("EventMember", back_populates="event",cascade = "all, delete-orphan")

class EventMember(Base):
    __tablename__ = "event_members"
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    role: Mapped[EventRole] = mapped_column(Enum(EventRole), default=EventRole.MEMBER)

    event: Mapped["Event"] = relationship("Event", back_populates="members")
    user: Mapped["User"] = relationship("User", back_populates="event_members")

    __table_args__ = (
        UniqueConstraint('event_id', 'user_id', name='uq_event_user'),
    )   
