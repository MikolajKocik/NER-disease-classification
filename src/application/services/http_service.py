from domain.abstractions.ner_service import NERService
from domain.entities.model_config import ModelConfig
from application.schemas.ner_response import NERResponse
from application.schemas.ner_request import NERRequest

import httpx

class HttpService(NERService):
    def __init__(self, config: ModelConfig):
        self._config = config
        
    async def predict(self, req: NERRequest) -> NERResponse:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=f"{self._config.endpoint}/{self._config.version}/predict",
                data=req
            )
        
        response.raise_for_status()
        
        data = response.json()
        return NERResponse(**data)
        
        