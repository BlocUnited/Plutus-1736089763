from bson import ObjectId
from pydantic import BaseModel, Field

class Achievement(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    user_id: ObjectId = Field(..., description='Reference to the user')
    achievement_title: str
    description: str
    date_awarded: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
