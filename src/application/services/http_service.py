from domain.abstractions.ner_service import NERService
from domain.entities.model_config import ModelConfig
from application.schemas.ner_response import NERResponse
from application.schemas.ner_request import NERRequest

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import httpx

class HttpService(NERService):
    def __init__(self, config: ModelConfig):
        self._config = config
        
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((httpx.ReadTimeout, httpx.ConnectError))
    )
    async def predict(self, req: NERRequest) -> NERResponse:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=f"{self._config.endpoint}/{self._config.version}/predict",
                data=req
            )
        
        response.raise_for_status()
        
        data = response.json()
        return NERResponse(**data)
        
        