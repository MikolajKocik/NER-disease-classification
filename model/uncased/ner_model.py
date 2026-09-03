from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

class BertUncased():
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            ".saved/un-ner.model"
        )
        self.model = AutoModelForTokenClassification.from_pretrained(
            ".saved/un-ner.model",
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
        return results
