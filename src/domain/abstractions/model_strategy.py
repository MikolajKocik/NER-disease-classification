from abc import ABC, abstractmethod

from application.schemas.ner_request import NERRequest
from application.schemas.ner_response import NERResponse

class ModelStrategy(ABC):
    """
    Strategy interface declares which model to use for medical entity recognition

    The Context uses this interface to call the model by concrete strategy
    """
    
    @abstractmethod
    async def predict(self, req: NERRequest) -> NERResponse:
        pass
    
        