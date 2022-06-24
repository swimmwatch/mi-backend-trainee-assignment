"""
Database configuration.
"""
from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    db_user: str = 'postgres'
    db_password: str = ''
    db_name: str = ''
    db_host: str = 'localhost'
    db_scheme: str = 'postgresql+asyncpg'

    @property
    def db_url(self):
        return f'{self.db_scheme}://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}'


database_settings = DatabaseSettings()
