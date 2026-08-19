from fastapi import APIRouter,HTTPException
from app.schemas.invitation import InvitationCreate, InvitationResponse

router = APIRouter(tags=["invitations"])

@router.post("/events/{event_id}/invitations", response_model=InvitationResponse)
async def create_invitaion(event_id: str, invitation: InvitationCreate):
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.patch("/invitations/{invitation_id}", response_model=InvitationResponse)
async def update_invitation_status(invitation_id: str):
    raise HTTPException(status_code=501, detail="Not Implemented")
