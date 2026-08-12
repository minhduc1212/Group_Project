from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey, UniqueConstraint
from typing import Optional
from .base import Base
from .enums import VoteValue
    
class PlanVote(Base):
    __tablename__ = "plan_votes"
        
    plan_id: Mapped[str] = mapped_column(ForeignKey("plans.id", ondelete="CASCADE"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    value: Mapped[VoteValue] = mapped_column(Enum(VoteValue))
    comment: Mapped[Optional[str]] = mapped_column(String, nullable=True)
        
    __table_args__ = (
        UniqueConstraint('plan_id', 'user_id', name='uq_plan_user_vote'),
    )
