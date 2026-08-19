from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime
from decimal import Decimal

class SettlementBase(BaseModel):
    amount: Decimal = Field(..., gt=0, description="Settlement amount must be greater than zero")

class SettlementCreate(SettlementBase):
    from_user_id: str
    to_user_id: str

    @model_validator(mode='after')
    def validate_different_users(self) -> "SettlementCreate":
        """Rejects requests where a user is assigned a debt to themselves."""
        if self.from_user_id == self.to_user_id:
            raise ValueError("The debtor (from_user) and creditor (to_user) cannot be the same person.")
        return self

class SettlementResponse(SettlementBase):
    id: str
    event_id: str
    from_user_id: str
    to_user_id: str
    is_settled: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SettlementUpdate(BaseModel):
    is_settled: bool