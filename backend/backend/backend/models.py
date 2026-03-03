from pydantic import BaseModel
from datetime import datetime


class ComplaintCreate(BaseModel):
    title: str
    description: str
    contract_id: str
    impact_level: int
    probability_level: int


class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    contract_id: str
    impact_level: int
    probability_level: int
    risk_score: int
    risk_level: str
    recommended_action: str
    created_at: datetime
