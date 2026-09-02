from fastapi import APIRouter, Depends

from domain.abstractions import Context, ModelStrategy
from api.extensions.dependencies import get_strategy
from application.schemas.ner_request import NERRequest
from application.schemas.ner_response import NERResponse

router = APIRouter()

@router.post("/predict", response_model=NERResponse)
async def predict(
    req: NERRequest,
    strategy: ModelStrategy = Depends(get_strategy)
):
    context = Context(strategy)

    return await context.predict_disease(req)