from fastapi import FastAPI

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