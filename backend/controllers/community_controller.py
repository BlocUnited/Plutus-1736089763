from fastapi import APIRouter, Depends, HTTPException
from backend.models.communities import Community
from backend.services.community_service import CommunityService

router = APIRouter()

@router.post('/communities', response_model=str)
async def create_community(community: Community, community_service: CommunityService = Depends()):
    return await community_service.create_community(community)

@router.get('/communities/{community_id}', response_model=Community)
async def get_community(community_id: str, community_service: CommunityService = Depends()):
    return await community_service.get_community(community_id)

@router.put('/communities/{community_id}', response_model=dict)
async def update_community(community_id: str, community: Community, community_service: CommunityService = Depends()):
    return await community_service.update_community(community_id, community)

@router.delete('/communities/{community_id}', response_model=dict)
async def delete_community(community_id: str, community_service: CommunityService = Depends()):
    return await community_service.delete_community(community_id)
