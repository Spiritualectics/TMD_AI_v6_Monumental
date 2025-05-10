from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tmd_core_v6_monumental import generate_tmd_forecast_v6
import hashlib
import os

API_SECRET_KEY = os.getenv("API_SECRET_KEY")
API_SIGNATURE_HASH = hashlib.sha256(API_SECRET_KEY.encode()).hexdigest()

app = FastAPI(
    title="TMD-AI Monumental Forecast",
    version="6.2",
    description="Phase 2 expansion – Terminal Manner Doctrine"
)

class TMDInput(BaseModel):
    energetic_integrity: float
    emotional_instability: float
    symbolic_density: float
    spiritual_pol: str
    guilt_load: float
    dominant_emotion: str
    archetype: str
    cause_affiliation: str
    location_risk: str
    final_event_imprint: str
    public_perception: str
    dream_symbol: str
    karmic_loop: str

def verify_signature(client_key: str):
    return hashlib.sha256(client_key.encode()).hexdigest() == API_SIGNATURE_HASH

@app.post("/predict")
def predict(input: TMDInput):
    if not verify_signature(API_SECRET_KEY):
        raise HTTPException(status_code=403, detail="Invalid API key")
    return generate_tmd_forecast_v6(input)
