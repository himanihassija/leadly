from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Leadly")
leads = []

class Lead(BaseModel):
    name: str
    work_email: str

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.post("/v2/leads")
def create_lead(lead: Lead):
    new = {"id": len(leads) + 1, "name": lead.name, "work_email": lead.work_email}
    leads.append(new)
    return new

@app.get("/v2/leads")
def list_leads():
    return leads
