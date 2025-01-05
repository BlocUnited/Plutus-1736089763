from fastapi import APIRouter, Depends, HTTPException
from backend.models.ai_mentors import AI_Mentor
from backend.services.ai_mentor_service import AIMentorService

router = APIRouter()

@router.post('/mentor', response_model=str)
async def create_ai_mentor(ai_mentor: AI_Mentor, ai_mentor_service: AIMentorService = Depends()):
    return await ai_mentor_service.create_ai_mentor(ai_mentor)

@router.get('/mentor/{user_id}', response_model=AI_Mentor)
async def get_ai_mentor(user_id: str, ai_mentor_service: AIMentorService = Depends()):
    return await ai_mentor_service.get_ai_mentor(user_id)
