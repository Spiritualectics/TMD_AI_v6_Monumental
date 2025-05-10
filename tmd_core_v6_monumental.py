def generate_tmd_forecast_v6(data):
    # Example scoring algorithm (simplified)
    score = (
        data.energetic_integrity
        - data.emotional_instability
        + data.symbolic_density
        + (1 if data.spiritual_pol == "Positive" else -1)
    )

    if score > 5:
        result = "Low Terminal Risk"
    elif score > 0:
        result = "Moderate Terminal Risk"
    else:
        result = "High Terminal Risk"

    return {
        "forecast": result,
        "score": round(score, 2),
        "inputs": data.dict()
    }
