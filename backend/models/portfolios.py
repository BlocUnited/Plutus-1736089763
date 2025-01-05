from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional

class ShowcaseItem(BaseModel):
    title: str
    description: str
    media: str
    created_at: str

class Portfolio(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    user_id: ObjectId = Field(..., description='Reference to the user')
    projects: List[ObjectId] = Field(default_factory=list, description='List of project ObjectIds')
    showcase: List[ShowcaseItem] = Field(default_factory=list, description='Showcase items')
    created_at: Optional[str] = Field(default=None, description='Creation timestamp')
    updated_at: Optional[str] = Field(default=None, description='Last update timestamp')

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
