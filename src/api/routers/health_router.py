from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Główny endpoint sprawdzający czy Gateway API żyje (Liveness probe).
    """
    return {
        "status": "ok", 
        "service": "medical-entity-recognition-gateway"
    }