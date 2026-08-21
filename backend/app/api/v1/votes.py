from fastapi import APIRouter,HTTPException
from app.schemas.vote import PlanVoteCreate, PlanVoteResponse

router = APIRouter(tags=["votes"])

@router.post("/events/{event_id}/plans/{plan_id}/votes", response_model=PlanVoteResponse)
async def vote_plan(event_id: str,plan_id:str, vote:PlanVoteCreate):
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")

