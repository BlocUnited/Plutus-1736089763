from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class User(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    username: str = Field(..., unique=True)
    email: EmailStr = Field(..., unique=True)
    password: str
    portfolio: Optional[ObjectId] = Field(default=None, description='Reference to the user portfolio')
    communities: List[ObjectId] = Field(default_factory=list, description='List of community ObjectIds')
    achievements: List[ObjectId] = Field(default_factory=list, description='List of achievement ObjectIds')
    leaderboard: Optional[ObjectId] = Field(default=None, description='Reference to the leaderboard')
    dashboard: Optional[ObjectId] = Field(default=None, description='Reference to the user dashboard')
    mentor: Optional[ObjectId] = Field(default=None, description='Reference to the AI mentor')
    created_at: Optional[str] = Field(default=None, description='Creation timestamp')
    updated_at: Optional[str] = Field(default=None, description='Last update timestamp')

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
