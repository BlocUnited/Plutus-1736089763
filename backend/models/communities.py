from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional

class Community(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    name: str
    description: str
    category: str
    members: List[ObjectId] = Field(default_factory=list, description='List of user ObjectIds')
    discussions: List[ObjectId] = Field(default_factory=list, description='List of discussion ObjectIds')
    resources: List[ObjectId] = Field(default_factory=list, description='List of resource ObjectIds')

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
