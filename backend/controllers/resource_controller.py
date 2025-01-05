from fastapi import APIRouter, Depends, HTTPException
from backend.models.resources import Resource
from backend.services.resource_service import ResourceService

router = APIRouter()

@router.post('/resources', response_model=str)
async def add_resource(resource: Resource, resource_service: ResourceService = Depends()):
    return await resource_service.add_resource(resource)

@router.get('/resources/{community_id}', response_model=List[Resource])
async def get_resources(community_id: str, resource_service: ResourceService = Depends()):
    return await resource_service.get_resources(community_id)
