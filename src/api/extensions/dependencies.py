from domain.entities.model_config import ModelConfig
from domain.abstractions.ner_service import NERService
from domain.abstractions.model_strategy import ModelStrategy

from application.services.http_service import HttpService
from application.services.grpc_service import GRPCService

from infrastructure.strategies.uncased_strategy import UnCasedStrategy
from infrastructure.strategies.cased_strategy import CasedStrategy

from functools import lru_cache
from fastapi import Depends

IS_CASED = True

@lru_cache
def get_model_config() -> ModelConfig:
    return ModelConfig.from_env()

def get_ner_service(
    config: ModelConfig = Depends(get_model_config)
) -> NERService:
    if config.protocol == "http":
        return HttpService(config)
    if config.protocol == "grpc":
        return GRPCService(config)
    raise ValueError(f"Unsupported model protocol: {config.protocol}")

def get_strategy(
    service: NERService = Depends(get_ner_service)
) -> ModelStrategy:
    if IS_CASED:
        return CasedStrategy(service)
    else:
        return UnCasedStrategy(service)