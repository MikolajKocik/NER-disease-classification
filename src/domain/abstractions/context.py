from __future__ import annotations

from application.schemas.ner_request import NERRequest
from application.schemas.ner_response import NERResponse
from .model_strategy import ModelStrategy

class Context():
    def __init__(self, strategy: ModelStrategy) -> None:
        self._strategy = strategy
        
    @property
    def strategy(self) -> ModelStrategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: ModelStrategy) -> None:
        self._strategy = strategy
        
    async def predict_disease(self, req: NERRequest) -> NERResponse:
        """
        Predict a disease by NER classification with BERT model
        """
        return await self._strategy.predict(req)