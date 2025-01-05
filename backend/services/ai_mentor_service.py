from fastapi import HTTPException
from bson import ObjectId
from backend.models.ai_mentors import AI_Mentor

class AIMentorService:
    def __init__(self, db):
        self.db = db

    async def create_ai_mentor(self, ai_mentor: AI_Mentor):
        ai_mentor_dict = ai_mentor.dict()
        ai_mentor_dict['created_at'] = str(datetime.utcnow())
        result = await self.db['AI_Mentors'].insert_one(ai_mentor_dict)
        return str(result.inserted_id)

    async def get_ai_mentor(self, user_id: str):
        ai_mentor = await self.db['AI_Mentors'].find_one({'user_id': ObjectId(user_id)})
        if not ai_mentor:
            raise HTTPException(status_code=404, detail='AI Mentor not found')
        return AI_Mentor.from_mongo(ai_mentor)
