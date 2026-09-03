from __future__ import annotations

from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(frozen=True)
class ModelConfig():
    endpoint: str 
    version: str
    protocol: str

    @classmethod
    def from_env(cls) -> ModelConfig:
        return cls(
            endpoint=os.getenv("MODEL_ENDPOINT", os.getenv("model_endpoint", "")),
            version=os.getenv("MODEL_VERSION", os.getenv("model_version", "v1")),
            protocol=os.getenv("MODEL_PROTOCOL", os.getenv("model_protocol", "http")).lower()
        )