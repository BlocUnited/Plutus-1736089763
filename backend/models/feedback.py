from bson import ObjectId
from pydantic import BaseModel, Field

class Feedback(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    project_id: ObjectId = Field(..., description='Reference to the project')
    user_id: ObjectId = Field(..., description='Reference to the user providing feedback')
    feedback_text: str
    created_at: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
