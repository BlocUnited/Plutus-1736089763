from fastapi import HTTPException
from bson import ObjectId
from backend.models.leaderboards import Leaderboard

class LeaderboardService:
    def __init__(self, db):
        self.db = db

    async def get_leaderboard(self, category: str):
        leaderboard = await self.db['Leaderboards'].find_one({'category': category})
        if not leaderboard:
            raise HTTPException(status_code=404, detail='Leaderboard not found')
        return Leaderboard.from_mongo(leaderboard)
