from fastapi import APIRouter, Depends, HTTPException
from backend.models.projects import Project
from backend.services.project_service import ProjectService

router = APIRouter()

@router.post('/projects', response_model=str)
async def create_project(project: Project, project_service: ProjectService = Depends()):
    return await project_service.create_project(project)

@router.get('/projects/{project_id}', response_model=Project)
async def get_project(project_id: str, project_service: ProjectService = Depends()):
    return await project_service.get_project(project_id)

@router.put('/projects/{project_id}', response_model=dict)
async def update_project(project_id: str, project: Project, project_service: ProjectService = Depends()):
    return await project_service.update_project(project_id, project)

@router.delete('/projects/{project_id}', response_model=dict)
async def delete_project(project_id: str, project_service: ProjectService = Depends()):
    return await project_service.delete_project(project_id)
