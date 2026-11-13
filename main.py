from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Leadly")
leads = []

class Lead(BaseModel):
    full_name: str
    work_email: str

@app.get("/ping")
def health():
    return {"status": "ok"}

@app.post("/v6/leads")
def create_lead(lead: Lead):
    new = {"id": len(leads) + 1, "full_name": lead.full_name, "work_email": lead.work_email}
    leads.append(new)
    return new

@app.get("/v6/leads")
def list_leads():
    return leads
