from fastapi import FastAPI
import json
from fastapi import HTTPException
app = FastAPI()

def load_data():
    with open('testt.json') as f:
        data = json.load(f)
    return data
@app.get("/")
def read_root():
    return {"Hello": "Smart Public Transport API"}

@app.get("/data")
def get_data():
    data = load_data()
    return data 

@app.get("/data/{device_id}")
def get_item(device_id: str):
    data=load_data()
    filtered = [record for record in data if record["device_id"] == device_id]
    
    if filtered:
        return filtered
    available = list(set(r["device_id"] for r in data))

    raise HTTPException(
        status_code=404,
        detail={"error": "Device ID not found", "available_ids": list(data.keys())}
    )