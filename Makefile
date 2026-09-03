.PHONY: run check format proto

# run main app locally
run:
	uvicorn src.api.main:app --reload

# checks linter issues
check:
	mypy src/ model/
	ruff check src/ model/

# auto-formatting
format:
	ruff format src/ model/

# generate Python protobuf and gRPC modules
proto:
	.venv/bin/python -m grpc_tools.protoc \
		-I src/infrastructure/grpc/proto \
		--python_out=src/infrastructure/grpc/generated \
		--grpc_python_out=src/infrastructure/grpc/generated \
		src/infrastructure/grpc/proto/ner.proto
	sed -i 's/^import ner_pb2 as ner__pb2/from . import ner_pb2 as ner__pb2/' \
		src/infrastructure/grpc/generated/ner_pb2_grpc.py
