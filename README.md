# The project purpose
The purpose of this project is to analyze and evaluate two different BERT models using NER approach on medical entities, where one of them is an uncased and sthe other one cased.

Cased preserve the letter casing.
Uncased does not do that.

The main goal is to check whether preserving letter casing affects the model's ability to understand the labels such as `DISEASE` and `CHEMICAL`. The results from both models will be compared on the same test dataset and metrics.

## How does it work?
Each model was trained on the BC5DR dataset from hugging face datasets and uses a token classification in the BIO schema:

```text
O, B-Disease, I-Disease, B-Chemical, I-Chemical
```

## Requirements

- Python >=3.11 ;
- Docker engine

# A quick usage example
Predictions:

```bash
curl -X POST http://localhost:8000/v1/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Patient has diabetes."}'
```

response example:

```json
{
  "entities": [
    {
      "text": "diabetes",
      "label": "DISEASE",
      "start": 13,
      "end": 21,
      "confidence": 0.97
    }
  ]
}
```

>[!IMPORTANT]
>Before run the containers, the model should be already trained in `model/saved` directory.
>The models' images copy these artifacts during the build process, therefore after training its important to build the containers again:

```bash
docker compose build
docker compose up
```
