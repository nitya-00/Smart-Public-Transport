from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import buses, health

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(buses.router, prefix="/buses", tags=["buses"])
app.include_router(health.router, prefix="/health", tags=["health"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Public Bus API"}