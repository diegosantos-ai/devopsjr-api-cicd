from datetime import datetime, timezone
import os

from fastapi import FastAPI

APP_NAME = "devopsjr-api-cicd"
APP_VERSION = "0.1.0"
APP_ENV = os.getenv("APP_ENV", "dev")

app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/")
def root():
    return {
        "message": f"Bem-vindo à API {APP_NAME}",
        "service": APP_NAME,
        "version": APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": APP_NAME,
    }


@app.get("/info")
def info():
    return {
        "project": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }