from fastapi import APIRouter, Depends, HTTPException
from backend.models.dashboards import Dashboard
from backend.services.dashboard_service import DashboardService

router = APIRouter()

@router.get('/dashboard/{user_id}', response_model=Dashboard)
async def get_dashboard(user_id: str, dashboard_service: DashboardService = Depends()):
    return await dashboard_service.get_dashboard(user_id)
