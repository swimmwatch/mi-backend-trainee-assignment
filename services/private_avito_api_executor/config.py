"""
Private Avito API executor service configuration.
"""
from pydantic import BaseSettings


class PrivateAvitoApiExecutorSettings(BaseSettings):
    grpc_server_addr: str
    avito_magic_key: str


private_avito_api_executor_settings = PrivateAvitoApiExecutorSettings()
