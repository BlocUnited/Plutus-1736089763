from bson import ObjectId
from pydantic import BaseModel, Field

class AI_Mentor(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    user_id: ObjectId = Field(..., description='Reference to the user')
    preferences: dict = Field(..., description='User preferences for AI mentor')
    created_at: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
