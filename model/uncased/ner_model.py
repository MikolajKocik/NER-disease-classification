from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "saved" / "un-ner.model"

class BertUncased():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_PATH
        )
        self.model = AutoModelForTokenClassification.from_pretrained(
            MODEL_PATH,
            device_map="auto",
            attn_implementation="sdpa"
        )
        self.ner_pipeline = pipeline(
            "ner",
            model=self.model,
            tokenizer=self.tokenizer,
            aggregation_strategy="simple"
        )

    def recognize(self, text: str):
        """
        Identify and categorize named entities based on context 
        with uncased approach and trained knowledge
        """
        results = self.ner_pipeline(text)
        return [
            {
                "text": entity["word"],
                "label": entity["entity_group"].upper(),
                "start": entity["start"],
                "end": entity["end"],
                "confidence": entity["score"],
            }
            for entity in results
        ]
