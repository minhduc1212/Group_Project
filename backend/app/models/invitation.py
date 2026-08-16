from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey, DateTime, CheckConstraint
from typing import Optional
from datetime import datetime
from .base import Base
from .enums import InvitationStatus
    
class Invitation(Base):
    __tablename__ = "invitations"
        
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"))
    invited_by: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    email: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    invited_user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id", 
 ondelete="SET NULL"), nullable=True)
    status: Mapped[InvitationStatus] = mapped_column(Enum(InvitationStatus),default=InvitationStatus.PENDING)
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    __table_args__ = (
        CheckConstraint(
            'email IS NOT NULL OR invited_user_id IS NOT NULL', 
            name='chk_invite_target_exists'
        ),
    )

