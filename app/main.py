from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="devopsjr-api-cicd", version="0.1.0")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "devopsjr-api-cicd",
    }


@app.get("/info")
def info():
    return {
        "project": "devopsjr-api-cicd",
        "version": "0.1.0",
        "environment": "dev",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }