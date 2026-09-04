from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import logging
import os
import time

from api.routers.predict_router import router as predict_router
from api.routers.health_router import router as health_router
from api.extensions.rate_limiter import limiter

from domain.exceptions.unavailable_ex import ModelUnavailableException
from domain.exceptions.internal_ex import InternalException

app = FastAPI(
    title="Medical entity recognition service",
    description="API to serve and eval the BERT models",
    version="1.0.0"
)

API_VERSION = os.getenv("API_VERSION", os.getenv("api_version", "v1"))

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("ner-gateway")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"- Status: {response.status_code} "
        f"- {process_time:.4f}s"
    )
    return response

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

app.include_router(predict_router, prefix=f"/{API_VERSION}")
app.include_router(health_router, prefix=f"/{API_VERSION}")