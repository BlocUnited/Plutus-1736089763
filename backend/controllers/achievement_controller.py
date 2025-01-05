from fastapi import APIRouter, Depends, HTTPException
from backend.models.achievements import Achievement
from backend.services.achievement_service import AchievementService

router = APIRouter()

@router.post('/achievements', response_model=str)
async def award_achievement(achievement: Achievement, achievement_service: AchievementService = Depends()):
    return await achievement_service.award_achievement(achievement)

@router.get('/achievements/{user_id}', response_model=List[Achievement])
async def get_user_achievements(user_id: str, achievement_service: AchievementService = Depends()):
    return await achievement_service.get_user_achievements(user_id)
