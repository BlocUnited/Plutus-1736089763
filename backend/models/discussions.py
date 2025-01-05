from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional

class Discussion(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    community_id: ObjectId = Field(..., description='Reference to the community')
    user_id: ObjectId = Field(..., description='Reference to the user who created the discussion')
    content: str
    replies: List[ObjectId] = Field(default_factory=list, description='List of reply ObjectIds')
    created_at: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
