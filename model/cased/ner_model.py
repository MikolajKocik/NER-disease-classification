from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

class BertCased():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            ".saved/c-ner_model"
        )
        self.model = AutoModelForTokenClassification.from_pretrained(
            ".saved/c-ner.model",
            device_map="auto",
            attn_implementation="sdpa"
        )
        self.ner_pipeline = pipeline(
            "ner",
            model=self.model,
            tokenizer=self.tokenizer,
            aggregation_strategy="simple"
        )

    def recognize(self, text: str) -> list[dict]:
        """
        Identify and categorize named entities based on context 
        with cased approach and trained knowledge
        """
        results = self.ner_pipeline(text)
        return results
