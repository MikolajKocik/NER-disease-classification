from domain.entities.disease_type import DiseaseType

from pydantic import BaseModel

class Entity(BaseModel):
    text: str
    label: DiseaseType
    start: int
    end: int
    confidence: float

class NERResponse(BaseModel):
    entities: list[Entity]