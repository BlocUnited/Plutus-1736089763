from fastapi import HTTPException
from bson import ObjectId
from backend.models.achievements import Achievement

class AchievementService:
    def __init__(self, db):
        self.db = db

    async def award_achievement(self, achievement: Achievement):
        achievement_dict = achievement.dict()
        achievement_dict['date_awarded'] = str(datetime.utcnow())
        result = await self.db['Achievements'].insert_one(achievement_dict)
        return str(result.inserted_id)

    async def get_user_achievements(self, user_id: str):
        achievements = await self.db['Achievements'].find({'user_id': ObjectId(user_id)}).to_list(length=100)
        return [Achievement.from_mongo(achievement) for achievement in achievements]
