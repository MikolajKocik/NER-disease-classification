from abc import ABC, abstractmethod

from application.schemas.ner_request import NERRequest

class NERService(ABC):
    """
    Abstract interface for dedicated net protocol
    
    For instance you can use HTTP or gRPC 
    """
    
    @abstractmethod
    async def predict(self, req: NERRequest):
        pass