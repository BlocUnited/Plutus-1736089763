from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List

class Leaderboard(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    category: str
    rankings: List[dict] = Field(default_factory=list, description='List of user rankings')

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
