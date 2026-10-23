"""Backend reads ASTRA_BASE_PATH (injected by the platform under path-based
routing) and mounts the API router under it."""
import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

BASE_PATH = os.environ.get("ASTRA_BASE_PATH", "").rstrip("/")

app = FastAPI()


@app.get(BASE_PATH + "/api/hello")
async def hello() -> dict:
    return {"message": "hello from python backend"}


@app.get(BASE_PATH + "/health")
async def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})
