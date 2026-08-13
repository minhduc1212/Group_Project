from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum, ForeignKey, Numeric, UniqueConstraint
from typing import List, Optional
from .base import Base
from .enums import ExpenseType, SplitType, StopCategory
    
class Expense(Base):
    __tablename__ = "expenses"
        
    event_id: Mapped[str] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"),
index=True)
    plan_stop_id: Mapped[Optional[str]] = mapped_column(ForeignKey("plan_stops.id",
ondelete="SET NULL"), nullable=True)
    paid_by_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(Numeric)
    type: Mapped[ExpenseType] = mapped_column(Enum(ExpenseType), default=ExpenseType.
PAYMENT)
    category: Mapped[Optional[StopCategory]] = mapped_column(Enum(StopCategory),
nullable=True)
    split_type: Mapped[SplitType] = mapped_column(Enum(SplitType), default=SplitType.EQUAL)
    note: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    receipt_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
        
    splits: Mapped[List["ExpenseSplit"]] = relationship("ExpenseSplit",
back_populates="expense", cascade="all, delete-orphan")
    
class ExpenseSplit(Base):
    __tablename__ = "expense_splits"
        
    expense_id: Mapped[str] = mapped_column(ForeignKey("expenses.id", ondelete="CASCADE"))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    amount: Mapped[float] = mapped_column(Numeric)
        
    expense: Mapped["Expense"] = relationship("Expense", back_populates="splits")
        
    __table_args__ = (
    UniqueConstraint('expense_id', 'user_id', name='uq_expense_user_split'),
    )