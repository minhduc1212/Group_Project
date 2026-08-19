from fastapi import APIRouter,HTTPException
from typing import List
from app.schemas.event import EventCreate, EventResponse

router = APIRouter(prefix="/events", tags=["events"])

@router.get("",response_model=List[EventResponse])
async def list_events():
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.post("",response_model=EventResponse)
async def create_event(event: EventCreate):
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.patch("/{event_id}")
async def update_event(event_id: str, event_update: EventCreate):
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")
