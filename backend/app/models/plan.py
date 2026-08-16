from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey, Boolean, Numeric, Float, JSON, DateTime,Integer
from typing import List, Optional, Any, Dict
from datetime import datetime
from .base import Base
from .enums import StopCategory


class Plan(Base):
    __tablename__ = "plans"

    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String)
    is_ai_generated: Mapped[bool] = mapped_column(Boolean, default=False)
    total_budget: Mapped[Optional[float]] = mapped_column(Numeric, nullable=True)
    created_by_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id",
ondelete="SET NULL"), nullable=True)

    stops: Mapped[List["PlanStop"]] = relationship("PlanStop", back_populates="plan",cascade="all, delete-orphan")

class PlanStop(Base):
    __tablename__ = "plan_stops"

    plan_id: Mapped[str] = mapped_column(ForeignKey("plans.id", ondelete="CASCADE"))
    order: Mapped[int] = mapped_column(Integer)
    place_name: Mapped[str] = mapped_column(String)
    place_ref_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    lat: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    lng: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    note: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    estimated_cost: Mapped[Optional[float]] = mapped_column(Numeric, nullable=True)
    category: Mapped[Optional[StopCategory]] = mapped_column(Enum(StopCategory),nullable=True)
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    duration_minutes: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    metadata_: Mapped[Optional[Dict[str, Any]]] = mapped_column("metadata", JSON, nullable=True)

    # Allows you to instantly access all the votes cast on a specific itinerary
    votes: Mapped[List["PlanVote"]] = relationship("PlanVote", cascade="all, delete-orphan")
        
    plan: Mapped["Plan"] = relationship("Plan", back_populates="stops")