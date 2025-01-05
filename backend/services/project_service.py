from fastapi import HTTPException
from bson import ObjectId
from typing import List
from backend.models.projects import Project

class ProjectService:
    def __init__(self, db):
        self.db = db

    async def create_project(self, project: Project):
        project_dict = project.dict()
        project_dict['created_at'] = project_dict['updated_at'] = str(datetime.utcnow())
        result = await self.db['Projects'].insert_one(project_dict)
        return str(result.inserted_id)

    async def get_project(self, project_id: str):
        project = await self.db['Projects'].find_one({'_id': ObjectId(project_id)})
        if not project:
            raise HTTPException(status_code=404, detail='Project not found')
        return Project.from_mongo(project)

    async def update_project(self, project_id: str, project_data: Project):
        result = await self.db['Projects'].update_one({'_id': ObjectId(project_id)}, {'$set': project_data.dict(exclude_unset=True)})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail='Project not found or no changes made')
        return {'message': 'Project updated successfully'}

    async def delete_project(self, project_id: str):
        result = await self.db['Projects'].delete_one({'_id': ObjectId(project_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail='Project not found')
        return {'message': 'Project deleted successfully'}
