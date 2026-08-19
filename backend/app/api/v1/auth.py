from fastapi import APIRouter,HTTPException
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/login/google",response_model=UserResponse)
async def register(user: UserCreate):
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/refresh-token")
async def refresh_token():
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/forgot-password")
async def forgot_password(email: str):
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/users/me", response_model=UserResponse)
async def get_profile():
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/users/me", response_model=UserResponse)
async def update_profile():
    raise HTTPException(status_code=501, detail="Not Implemented")