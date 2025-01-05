from bson import ObjectId
from pydantic import BaseModel, Field

class Resource(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='_id')  # MongoDB ObjectId
    community_id: ObjectId = Field(..., description='Reference to the community')
    title: str
    link: str
    description: str
    created_at: str

    class Config:
        json_encoders = {ObjectId: str}

    @classmethod
    def from_mongo(cls, data):
        return cls(**data)
