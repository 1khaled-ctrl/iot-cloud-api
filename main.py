from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
import logging



app = FastAPI(title="IoT Telemetry API")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("telemetry")



class TelemetryData(BaseModel):
    device_id: str = Field(..., min_length=1, max_length=64)
    temperature: float = Field(..., ge=-50, le=150)
    humidity: float = Field(..., ge=0, le=100)
    timestamp: datetime



telemetry_store: List[TelemetryData] = []



@app.get("/")
def root():
    return {"message": "IoT Telemetry API is running", "status": "ok"}


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/telemetry")
def receive_telemetry(data: TelemetryData):
    telemetry_store.append(data)
    logger.info(f"Telemetry received from {data.device_id}")

    return {
        "ok": True,
        "stored_records": len(telemetry_store),
        "data": data.model_dump()
    }


@app.get("/telemetry")
def list_telemetry(limit: int = 50):
    return {
        "count": len(telemetry_store),
        "items": [t.model_dump() for t in telemetry_store[-limit:]]
    }