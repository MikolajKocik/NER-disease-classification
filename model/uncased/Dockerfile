FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY model ./model
COPY src ./src

RUN pip install --no-cache-dir .

ENV PYTHONPATH=/app/src

WORKDIR /app/model/uncased

CMD ["sh", "-c", "if [ \"$MODEL_PROTOCOL\" = \"grpc\" ]; then exec python grpc_server.py; else exec uvicorn api:app --host 0.0.0.0 --port 8000; fi"]