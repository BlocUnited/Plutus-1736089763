from fastapi import APIRouter, Depends, HTTPException
from backend.models.feedback import Feedback
from backend.services.feedback_service import FeedbackService

router = APIRouter()

@router.post('/feedback', response_model=str)
async def submit_feedback(feedback: Feedback, feedback_service: FeedbackService = Depends()):
    return await feedback_service.submit_feedback(feedback)

@router.get('/feedback/{project_id}', response_model=List[Feedback])
async def get_feedback(project_id: str, feedback_service: FeedbackService = Depends()):
    return await feedback_service.get_feedback(project_id)
