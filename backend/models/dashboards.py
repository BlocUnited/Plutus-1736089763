from bson import ObjectId
from pydantic import BaseModel, Field

class Dashboard(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    user_id: ObjectId = Field(..., description='Reference to the user')
    progress: dict = Field(..., description='User progress metrics')
    created_at: str
    updated_at: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
