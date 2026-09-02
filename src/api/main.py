from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

from api.routers.predict_router import router as predict_router
from api.routers.health_router import router as health_router

from domain.exceptions.unavailable_ex import ModelUnavailableException
from domain.exceptions.internal_ex import InternalException

logger = logging.getLogger(__name__)

app = FastAPI(
    title="NER disease classification service",
    description="API to serve and eval the BERT models",
    version="1.0.0"
)

@app.exception_handler(ModelUnavailableException)
async def model_unavailable_exception_handler(request: Request, exc: ModelUnavailableException):
    return JSONResponse(
        status_code=503,
        content={"error": "Service Unavailable", "message": exc.message},
    )

@app.exception_handler(InternalException)
async def internal_server_exception_handler(request: Request, exc: InternalException):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "message": exc.message}
    )

app.include_router(predict_router)
app.include_router(health_router)