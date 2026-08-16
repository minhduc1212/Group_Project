from sqlalchemy import CheckConstraint
from sqlalchemy import UniqueConstraint
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Numeric, Boolean
from .base import Base
    
class Settlement(Base):
    __tablename__ = "settlements"
        
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"),
  index=True)
    from_user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    to_user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    is_settled: Mapped[bool] = mapped_column(Boolean, default=False)

    
    __table_args__ = (
        # Block users from owing themselves
        CheckConstraint(
            'from_user_id != to_user_id', 
            name='chk_no_self_debt'
        ),
        # Keep only one consolidated debt record between two users per trip
        UniqueConstraint(
            'event_id', 'from_user_id', 'to_user_id', 
            name='uq_event_user_settlement'
        ),
    )