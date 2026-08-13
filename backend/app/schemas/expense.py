from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.enums import ExpenseType, SplitType, StopCategory

# --- Expense ---
class ExpenseBase(BaseModel):
    title: str
    amount: float
    type: ExpenseType = ExpenseType.PAYMENT
    category: Optional[StopCategory] = None
    split_type: SplitType = SplitType.EQUAL
    note: Optional[str] = None
    receipt_url: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    plan_stop_id: Optional[str] = None
    paid_by_id: str

class ExpenseResponse(ExpenseBase):
    id: str
    event_id: str
    paid_by_id: str
    plan_stop_id: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# --- ExpenseSplit ---
class ExpenseSplitBase(BaseModel):
    amount: float

class ExpenseSplitCreate(ExpenseSplitBase):
    user_id: str

class ExpenseSplitResponse(ExpenseSplitBase):
    id: str
    expense_id: str
    user_id: str

    model_config = ConfigDict(from_attributes=True)
