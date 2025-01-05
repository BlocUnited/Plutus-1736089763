from fastapi import HTTPException
from bson import ObjectId
from typing import List
from backend.models.communities import Community

class CommunityService:
    def __init__(self, db):
        self.db = db

    async def create_community(self, community: Community):
        community_dict = community.dict()
        community_dict['created_at'] = community_dict['updated_at'] = str(datetime.utcnow())
        result = await self.db['Communities'].insert_one(community_dict)
        return str(result.inserted_id)

    async def get_community(self, community_id: str):
        community = await self.db['Communities'].find_one({'_id': ObjectId(community_id)})
        if not community:
            raise HTTPException(status_code=404, detail='Community not found')
        return Community.from_mongo(community)

    async def update_community(self, community_id: str, community_data: Community):
        result = await self.db['Communities'].update_one({'_id': ObjectId(community_id)}, {'$set': community_data.dict(exclude_unset=True)})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail='Community not found or no changes made')
        return {'message': 'Community updated successfully'}

    async def delete_community(self, community_id: str):
        result = await self.db['Communities'].delete_one({'_id': ObjectId(community_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail='Community not found')
        return {'message': 'Community deleted successfully'}
