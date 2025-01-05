from fastapi import APIRouter, Depends, HTTPException
from backend.models.discussions import Discussion
from backend.services.discussion_service import DiscussionService

router = APIRouter()

@router.post('/discussions', response_model=str)
async def create_discussion(discussion: Discussion, discussion_service: DiscussionService = Depends()):
    return await discussion_service.create_discussion(discussion)

@router.get('/discussions/{community_id}', response_model=List[Discussion])
async def get_discussions(community_id: str, discussion_service: DiscussionService = Depends()):
    return await discussion_service.get_discussions(community_id)
