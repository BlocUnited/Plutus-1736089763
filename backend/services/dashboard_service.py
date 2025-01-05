from fastapi import HTTPException
from bson import ObjectId
from backend.models.dashboards import Dashboard

class DashboardService:
    def __init__(self, db):
        self.db = db

    async def get_dashboard(self, user_id: str):
        dashboard = await self.db['Dashboards'].find_one({'user_id': ObjectId(user_id)})
        if not dashboard:
            raise HTTPException(status_code=404, detail='Dashboard not found')
        return Dashboard.from_mongo(dashboard)
