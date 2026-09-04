from domain.abstractions.model_strategy import ModelStrategy
from domain.abstractions.ner_service import NERService
from application.schemas.ner_request import NERRequest
from application.schemas.ner_response import NERResponse

class CasedStrategy(ModelStrategy):
    """
    Strategy for a cased BERT medical entity recognition model.
    Preserves text casing and delegates execution to the underlying NER service.
    """
    def __init__(self, service: NERService) -> None:
        self._service = service

    async def predict(self, req: NERRequest) -> NERResponse:
        return await self._service.predict(req)