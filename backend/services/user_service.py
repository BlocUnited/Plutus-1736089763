from fastapi import HTTPException, Depends
from bson import ObjectId
from typing import List
from backend.models.users import User
from backend.config.config import Config
from backend.middleware.middleware import Middleware

class UserService:
    def __init__(self, db):
        self.db = db

    async def register_user(self, user: User):
        # Check if user already exists
        existing_user = await self.db['Users'].find_one({'email': user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail='Email already registered')
        # Insert new user
        user_dict = user.dict()
        user_dict['created_at'] = user_dict['updated_at'] = str(datetime.utcnow())
        result = await self.db['Users'].insert_one(user_dict)
        return str(result.inserted_id)

    async def login_user(self, email: str, password: str):
        user = await self.db['Users'].find_one({'email': email})
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        # Validate password (hashing logic should be implemented)
        if user['password'] != password:
            raise HTTPException(status_code=403, detail='Invalid password')
        return {'message': 'Login successful', 'user_id': str(user['_id'])}

    async def get_user_profile(self, user_id: str):
        user = await self.db['Users'].find_one({'_id': ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        return User.from_mongo(user)

    async def update_user_profile(self, user_id: str, user_data: User):
        result = await self.db['Users'].update_one({'_id': ObjectId(user_id)}, {'$set': user_data.dict(exclude_unset=True)})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail='User not found or no changes made')
        return {'message': 'Profile updated successfully'}
