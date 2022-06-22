"""
Private Avito API executor service configuration.
"""
from pydantic import BaseSettings


class PrivateAvitoApiExecutorSettings(BaseSettings):
    grpc_server_addr: str
    avito_magick_key: str