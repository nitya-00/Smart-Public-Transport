from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.config import get_db

def get_current_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if bus is None:
        raise HTTPException(status_code=404, detail="Bus not found")
    return bus