from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime
from app.models.enums import ExpenseType, SplitType, StopCategory
from decimal import Decimal
# --- Expense ---
class ExpenseBase(BaseModel):
    title: str
    amount: Decimal = Field(..., gt=0, description="Total expense amount must be positive")
    type: ExpenseType = ExpenseType.PAYMENT
    category: Optional[StopCategory] = None
    split_type: SplitType = SplitType.EQUAL
    note: Optional[str] = None
    receipt_url: Optional[str] = None

class ExpenseCreate(ExpenseBase):
    plan_stop_id: Optional[str] = None
    paid_by_id: str
    splits: list["ExpenseSplitCreate"] = []

    from pydantic import model_validator
    
    @model_validator(mode='after')
    def validate_splits_total(self) -> "ExpenseCreate":
        if self.splits:
            total_splits = sum(split.amount for split in self.splits)
            if total_splits != self.amount:
                raise ValueError(f"Splits total ({total_splits}) must equal expense amount ({self.amount}).")
        return self

class ExpenseResponse(ExpenseBase):
    id: str
    event_id: str
    paid_by_id: str
    plan_stop_id: Optional[str] = None
    created_at: datetime
    splits: list["ExpenseSplitResponse"] = []

    model_config = ConfigDict(from_attributes=True)

# --- ExpenseSplit ---
class ExpenseSplitBase(BaseModel):
    # Enforces that the split amount must be strictly greater than 0
    amount: Decimal = Field(..., gt=0, description="Amount must be positive")

class ExpenseSplitCreate(ExpenseSplitBase):
    user_id: str

class ExpenseSplitResponse(ExpenseSplitBase):
    id: str
    expense_id: str
    user_id: str

    model_config = ConfigDict(from_attributes=True)
