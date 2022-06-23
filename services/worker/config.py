"""
Worker configuration.
"""
import os

from pydantic import BaseSettings

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL',
                                   'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND',
                                       'redis://localhost:6379')


class WorkerSettings(BaseSettings):
    private_avito_api_executor_grpc_server_addr: str = 'localhost:50051'


worker_settings = WorkerSettings()
