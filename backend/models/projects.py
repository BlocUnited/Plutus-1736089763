from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional

class Project(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    title: str
    description: str
    category: str
    collaborators: List[ObjectId] = Field(default_factory=list, description='List of user ObjectIds')
    created_at: Optional[str] = Field(default=None, description='Creation timestamp')
    updated_at: Optional[str] = Field(default=None, description='Last update timestamp')

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
