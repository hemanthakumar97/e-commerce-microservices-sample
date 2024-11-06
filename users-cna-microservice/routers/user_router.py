from typing import List, Optional, Any
from fastapi import APIRouter, Depends
from db.dals.user_dal import UserDAL
from db.models.user import User  # Import the SQLAlchemy model directly
from dependencies import get_user_dal

router = APIRouter()

@router.post("/users", response_model=None)  # Disable response model
async def create_user(name: str, email: str, mobile: str, user_dal: UserDAL = Depends(get_user_dal)):
    new_user = await user_dal.create_user(name, email, mobile)
    return new_user  # Return the SQLAlchemy model directly

@router.put("/users/{user_id}", response_model=None)  # Disable response model
async def update_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None, mobile: Optional[str] = None,
                      user_dal: UserDAL = Depends(get_user_dal)):
    await user_dal.update_user(user_id, name, email, mobile)
    return await user_dal.get_user(user_id)  # Return the updated user

@router.get("/users/{user_id}", response_model=None)  # Disable response model
async def get_user(user_id: int, user_dal: UserDAL = Depends(get_user_dal)) -> Any:
    return await user_dal.get_user(user_id)  # Return the user directly

@router.get("/users", response_model=None)  # Disable response model
async def get_all_users(user_dal: UserDAL = Depends(get_user_dal)) -> Any:
    users = await user_dal.get_all_users()
    return users  # Return the list of users directly
