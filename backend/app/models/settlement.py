from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Numeric, Boolean
from .base import Base
    
class Settlement(Base):
    __tablename__ = "settlements"
        
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"),
  index=True)
    from_user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    to_user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    amount: Mapped[float] = mapped_column(Numeric)
    is_settled: Mapped[bool] = mapped_column(Boolean, default=False)