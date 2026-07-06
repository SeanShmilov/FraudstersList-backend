from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import fraudsters

app = FastAPI(title="FraudstersList API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fraudsters.router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}
