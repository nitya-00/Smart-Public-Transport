from pydantic import BaseModel
from typing import List, Optional

class GPSPoint(BaseModel):
    latitude: float
    longitude: float
    timestamp: str

class Stop(BaseModel):
    id: int
    name: str
    location: GPSPoint

class Bus(BaseModel):
    id: int
    route: str
    current_stop: Stop
    crowd_level: Optional[str] = None
    gps_data: List[GPSPoint] = []