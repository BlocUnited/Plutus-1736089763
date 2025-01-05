from fastapi import HTTPException
from bson import ObjectId
from typing import List
from backend.models.resources import Resource

class ResourceService:
    def __init__(self, db):
        self.db = db

    async def add_resource(self, resource: Resource):
        resource_dict = resource.dict()
        resource_dict['created_at'] = str(datetime.utcnow())
        result = await self.db['Resources'].insert_one(resource_dict)
        return str(result.inserted_id)

    async def get_resources(self, community_id: str):
        resources = await self.db['Resources'].find({'community_id': ObjectId(community_id)}).to_list(length=100)
        return [Resource.from_mongo(resource) for resource in resources]
