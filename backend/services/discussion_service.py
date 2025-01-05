from fastapi import HTTPException
from bson import ObjectId
from typing import List
from backend.models.discussions import Discussion

class DiscussionService:
    def __init__(self, db):
        self.db = db

    async def create_discussion(self, discussion: Discussion):
        discussion_dict = discussion.dict()
        discussion_dict['created_at'] = str(datetime.utcnow())
        result = await self.db['Discussions'].insert_one(discussion_dict)
        return str(result.inserted_id)

    async def get_discussions(self, community_id: str):
        discussions = await self.db['Discussions'].find({'community_id': ObjectId(community_id)}).to_list(length=100)
        return [Discussion.from_mongo(discussion) for discussion in discussions]
