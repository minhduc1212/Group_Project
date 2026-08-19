from fastapi import APIRouter,HTTPException
from typing import Any

router = APIRouter(prefix= "/ai", tags=["ai"])

@router.get("/chat/stream", response_model=Any)
async def chat_stream():
    raise HTTPException(status_code=501, detail="Not Implemented")
