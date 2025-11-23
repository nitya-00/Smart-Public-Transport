from pydantic import BaseModel
from typing import List, Optional

class BusLiveOut(BaseModel):
    id: int
    route: str
    current_stop: str
    crowd_level: str

class CrowdResponse(BaseModel):
    bus_id: int
    crowd_level: str
    estimated_time: Optional[int]  # ETA in minutes

class BusTelemetry(BaseModel):
    bus_id: int
    latitude: float
    longitude: float
    timestamp: str  # ISO format datetime
    speed: float  # in km/h
    occupancy: int  # number of passengers