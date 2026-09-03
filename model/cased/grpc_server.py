import asyncio

import grpc

from infrastructure.grpc.generated import ner_pb2, ner_pb2_grpc
from ner_model import BertCased


class NERServicer(ner_pb2_grpc.NERServiceServicer):
    def __init__(self):
        self.model = BertCased()

    async def Predict(self, request, context):
        entities = self.model.recognize(request.text)
        return ner_pb2.NERResponse(
            entities=[
                ner_pb2.Entity(
                    text=entity["text"],
                    label=entity["label"],
                    start=entity["start"],
                    end=entity["end"],
                    confidence=entity["confidence"],
                )
                for entity in entities
            ]
        )


async def serve():
    server = grpc.aio.server()
    ner_pb2_grpc.add_NERServiceServicer_to_server(NERServicer(), server)
    server.add_insecure_port("[::]:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
