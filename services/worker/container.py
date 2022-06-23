"""
Worker DI container.
"""
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.wiring import providers
from redis.client import Redis

from services.private_avito_api_executor.grpc_client import PrivateAvitoApiExecutorGrpcClient
from services.redis.config import REDIS_HOST, REDIS_PORT
from services.worker.config import worker_settings


class WorkerContainer(DeclarativeContainer):
    redis_client = providers.Singleton(
        Redis,
        host=REDIS_HOST,
        port=REDIS_PORT
    )

    private_avito_api_executor_client = providers.Singleton(
        PrivateAvitoApiExecutorGrpcClient,
        worker_settings.private_avito_api_executor_grpc_server_addr
    )
