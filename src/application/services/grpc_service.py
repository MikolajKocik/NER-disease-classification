from domain.abstractions.ner_service import NERService
from domain.entities.model_config import ModelConfig
from application.schemas.ner_response import NERResponse
from application.schemas.ner_request import NERRequest
#from infrastructure.grpc.generated import ner_pb2
#from infrastructure.grpc.generated import ner_pb2_grpc

import grpc

class GRPCService(NERService):
    def __init__(self, config: ModelConfig):
        self._config = config
        
        self._channel = grpc.aio.secure_channel(
            self._config.endpoint
        )
        
        # self._stub = ner_pb2_grpc.NERServiceStub(
        #     self._channel
        # )
        
    # async def predict(self, req: NERRequest) -> NERResponse:
        
    #     grpc_request = ner_pb2.NERRequest(
    #         text=req.text
    #     )
        
    #     response = await self._stub.Predict(
    #         grpc_request
    #     )
        
    #     return NERResponse(
    #         entities=[
    #             {
    #                 "text": entity.text,
    #                 "label": entity.label,
    #                 "start": entity.start,
    #                 "end": entity.end,
    #                 "confidence": entity.confidence
    #             }
    #             for entity in response.entities
    #         ]
    #     )
        