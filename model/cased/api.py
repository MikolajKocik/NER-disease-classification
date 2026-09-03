from fastapi import FastAPI
from pydantic import BaseModel
from ner_model import BertCased        
import os

class Request(BaseModel):
    text: str

app = FastAPI(
    "BERT NER uncased service",
    version="1.0.0"
)

ner_model = BertCased()

version = os.getenv("model_version")

@app.post("/{version}/predict")
def predict(payload: Request):
    entities = ner_model.recognize(payload.text)
    return {"entities": entities}

@app.get("/health")
def health_check():
    return {"status": "ok"}
