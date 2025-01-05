from fastapi import APIRouter, Depends, HTTPException
from backend.models.users import User
from backend.services.user_service import UserService

router = APIRouter()

@router.post('/users/register', response_model=str)
async def register_user(user: User, user_service: UserService = Depends()):
    return await user_service.register_user(user)

@router.post('/users/login')
async def login_user(email: str, password: str, user_service: UserService = Depends()):
    return await user_service.login_user(email, password)

@router.get('/users/profile/{user_id}', response_model=User)
async def get_user_profile(user_id: str, user_service: UserService = Depends()):
    return await user_service.get_user_profile(user_id)

@router.put('/users/profile/{user_id}', response_model=dict)
async def update_user_profile(user_id: str, user: User, user_service: UserService = Depends()):
    return await user_service.update_user_profile(user_id, user)
