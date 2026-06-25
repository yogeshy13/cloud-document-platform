from fastapi import FastAPI
from app.core.config import settings

settings.DATABASE_URL

from app.db.database import Base

from app.db.database import engine

import app.db.models

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Cloud Document Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Cloud Document Platform API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }