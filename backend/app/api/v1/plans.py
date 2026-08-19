from fastapi import APIRouter , HTTPException
from typing import List
from app.schemas.plan import PlanCreate,PlanResponse,PlanStopCreate,PlanStopResponse
from app.models.enums import PlanStatus

router = APIRouter(tags=["plans"])

@router.post("/events/{event_id}/plans", response_model=PlanResponse)
async def create_plan(event_id: str, plan:PlanCreate):
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.patch("/events/{event_id}/plans/{plan_id}/stops", response_model=[PlanStopResponse])
async def update_plan_stops(event_id:str, plan_id:str, stops:List[PlanStopCreate]):
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.patch("/events/{event_id}/plans/{plan_id}/status", response_model=PlanResponse)
async def update_plan_status(event_id: str,plan_id:str,status:PlanStatus):
     raise HTTPException(status_code=501, detail="Not Implemented")
