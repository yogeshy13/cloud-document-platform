from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.documents import router as document_router

app = FastAPI(
    title="Cloud Document Platform",
)
app.include_router(document_router)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Cloud Document Platform"
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