from fastapi import HTTPException
from bson import ObjectId
from typing import List
from backend.models.feedback import Feedback

class FeedbackService:
    def __init__(self, db):
        self.db = db

    async def submit_feedback(self, feedback: Feedback):
        feedback_dict = feedback.dict()
        feedback_dict['created_at'] = str(datetime.utcnow())
        result = await self.db['Feedback'].insert_one(feedback_dict)
        return str(result.inserted_id)

    async def get_feedback(self, project_id: str):
        feedback_list = await self.db['Feedback'].find({'project_id': ObjectId(project_id)}).to_list(length=100)
        return [Feedback.from_mongo(feedback) for feedback in feedback_list]
