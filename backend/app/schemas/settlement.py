from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SettlementBase(BaseModel):
    amount: float

class SettlementCreate(SettlementBase):
    from_user_id: str
    to_user_id: str

class SettlementResponse(SettlementBase):
    id: str
    event_id: str
    from_user_id: str
    to_user_id: str
    is_settled: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
