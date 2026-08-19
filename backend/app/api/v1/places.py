from fastapi import APIRouter, HTTPException
from typing import Optional,Any

router = APIRouter(prefix="/places", tags=["places"])

@router.get("/search",response_model=Any)
async def search_places(category:Optional[str] = None):
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.get("/hotels/compare", response_model=Any)
async def compare_hotels(ids:str):
    raise HTTPException(status_code=501, detail="Not Implemented")
