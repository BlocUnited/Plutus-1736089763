from fastapi import APIRouter
from backend.controllers.user_controller import router as user_router
from backend.controllers.portfolio_controller import router as portfolio_router
from backend.controllers.community_controller import router as community_router
from backend.controllers.project_controller import router as project_router
from backend.controllers.feedback_controller import router as feedback_router
from backend.controllers.discussion_controller import router as discussion_router
from backend.controllers.resource_controller import router as resource_router
from backend.controllers.ai_mentor_controller import router as ai_mentor_router
from backend.controllers.achievement_controller import router as achievement_router
from backend.controllers.leaderboard_controller import router as leaderboard_router
from backend.controllers.dashboard_controller import router as dashboard_router

api_router = APIRouter()

# Include routers with a prefix
api_router.include_router(user_router, prefix='/users', tags=['users'])
api_router.include_router(portfolio_router, prefix='/portfolios', tags=['portfolios'])
api_router.include_router(community_router, prefix='/communities', tags=['communities'])
api_router.include_router(project_router, prefix='/projects', tags=['projects'])
api_router.include_router(feedback_router, prefix='/feedback', tags=['feedback'])
api_router.include_router(discussion_router, prefix='/discussions', tags=['discussions'])
api_router.include_router(resource_router, prefix='/resources', tags=['resources'])
api_router.include_router(ai_mentor_router, prefix='/mentor', tags=['ai_mentor'])
api_router.include_router(achievement_router, prefix='/achievements', tags=['achievements'])
api_router.include_router(leaderboard_router, prefix='/leaderboards', tags=['leaderboards'])
api_router.include_router(dashboard_router, prefix='/dashboard', tags=['dashboard'])
