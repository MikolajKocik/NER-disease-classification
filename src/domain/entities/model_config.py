from __future__ import annotations

from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(frozen=True)
class ModelConfig():
    endpoint: str 
    version: str

    @classmethod
    def from_env(cls) -> ModelConfig:
        return cls(
            endpoint=os.getenv("model_endpoint"),
            version=os.getenv("model_version")
        )