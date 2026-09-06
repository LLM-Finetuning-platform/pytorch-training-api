from collections.abc import AsyncIterator

from grpc.aio import ServicerContext

from src.api.v1.router import V1_router
import src.handlers.grpc.proto.v1.training_api_pb_grpc as training_api_pb_grpc
import src.handlers.grpc.proto.v1.training_api_pb as training_api_pb

class TrainingAPIService(training_api_pb_grpc.TrainingAPIServiceService):
    async def train(self, request: training_api_pb_grpc.TrainRequest, context: ServicerContext) -> training_api_pb_grpc.TrainResponse:
        # await  V1_router.execute("Train",request)
        return await super().train(request, context)
