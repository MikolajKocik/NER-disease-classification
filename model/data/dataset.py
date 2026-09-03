"""
Checks dataset and inspect the offsets if the labels are matched correctly
"""
from datasets import load_dataset

dataset = load_dataset(
    "bigbio/bc5cdr",
    name="bc5cdr_bigbio_kb",
    trust_remote_code=True
)

record = dataset["train"][0]
passages = record["passages"]

text = " ".join([p["text"][0] for p in passages])

for entity in record["entities"]:
    s, e = entity["offsets"][0]
    print(repr(entity["text"][0]), "|", repr(text[s:e]))