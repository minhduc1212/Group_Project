from fastapi import APIRouter,HTTPException
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/login/google",response_model=UserResponse)
async def login_google(user: UserCreate):
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/refresh-token")
async def refresh_token():
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.post("/forgot-password")
async def forgot_password(email: str):
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.get("/users/me", response_model=UserResponse)
async def get_profile():
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")
@router.patch("/users/me", response_model=UserResponse)
async def update_profile():
    """
    API endpoint skeleton.
    """
    raise HTTPException(status_code=501, detail="Not Implemented")