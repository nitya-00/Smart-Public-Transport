from pydantic import BaseModel
from typing import List, Optional

class ETAResponse(BaseModel):
    bus_id: str
    estimated_time: float  # ETA in minutes
    destination: str

class GPSIn(BaseModel):
    bus_id: str
    latitude: float
    longitude: float
    timestamp: Optional[str] = None  # Optional timestamp for the GPS data