
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tmd_api_v6_core import generate_tmd_forecast_v6
import hashlib
import os

API_SECRET_KEY = os.getenv("API_SECRET_KEY", "MISSING_KEY")
if API_SECRET_KEY == "MISSING_KEY":
    raise ValueError("Environment variable API_SECRET_KEY is not set.")

API_SIGNATURE_HASH = hashlib.sha256(API_SECRET_KEY.encode()).hexdigest()

app = FastAPI(
    title="TMD-AI Monumental Forecast",
    version="6.2",
    description="Phase 2 expansion – Terminal Manner Doctrine AI Engine"
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
    public_perception: str
    dream_symbol: str
    karmic_loop: str

@app.post("/predict")
def predict_tmd(data: TMDInput, api_signature: str):
    if hashlib.sha256(API_SECRET_KEY.encode()).hexdigest() != api_signature:
        raise HTTPException(status_code=403, detail="Invalid API signature")
    result = generate_tmd_forecast_v6(data)
    return {"forecast": result}
