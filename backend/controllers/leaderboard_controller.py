from fastapi import APIRouter, Depends, HTTPException
from backend.models.leaderboards import Leaderboard
from backend.services.leaderboard_service import LeaderboardService

router = APIRouter()

@router.get('/leaderboards/{category}', response_model=Leaderboard)
async def get_leaderboard(category: str, leaderboard_service: LeaderboardService = Depends()):
    return await leaderboard_service.get_leaderboard(category)
