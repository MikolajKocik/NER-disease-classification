from domain.abstractions import Context, ModelStrategy
from application.schemas.ner_request import NERRequest
from application.schemas.ner_response import NERResponse

class RecognitionHandler():
    def __init__(self, strategy: ModelStrategy):
        self.context = Context(strategy)
        
    async def handle_prediction(self, req: NERRequest) -> NERResponse:
        """
        Handler abstraction for model prediction
        Avoid context implementation in endpoint
        """
        return await self.context.predict_disease(req)