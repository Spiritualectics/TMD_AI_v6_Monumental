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
    description="Phase 2 expansion with full parameter support"
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
    api_signature: str

@app.post("/predict")
def generate_forecast(input: TMDInput):
    if hashlib.sha256(input.api_signature.encode()).hexdigest() != API_SIGNATURE_HASH:
        raise HTTPException(status_code=403, detail="Invalid API signature")

    forecast = generate_tmd_forecast_v6({
        "energetic_integrity": input.energetic_integrity,
        "emotional_instability": input.emotional_instability,
        "symbolic_density": input.symbolic_density,
        "spiritual_pol": input.spiritual_pol,
        "guilt_load": input.guilt_load,
        "dominant_emotion": input.dominant_emotion,
        "archetype": input.archetype,
        "cause_affiliation": input.cause_affiliation,
        "location_risk": input.location_risk,
        "final_event_imprint": input.final_event_imprint,
        "public_perception": input.public_perception,
        "dream_symbol": input.dream_symbol,
        "karmic_loop": input.karmic_loop
    })

    return {"forecast": forecast}
