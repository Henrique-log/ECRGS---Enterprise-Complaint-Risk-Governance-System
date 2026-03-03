from fastapi import FastAPI
from models import ComplaintCreate, ComplaintResponse
from risk_engine import calculate_risk
from database import save_complaint

app = FastAPI(title="ECRGS - Enterprise Complaint & Risk Governance System")

@app.post("/api/v1/complaints", response_model=ComplaintResponse)
def create_complaint(complaint: ComplaintCreate):

    risk = calculate_risk(
        complaint.impact_level,
        complaint.probability_level
    )

    complaint_data = complaint.dict()
    complaint_data.update(risk)

    saved = save_complaint(complaint_data)

    return saved
