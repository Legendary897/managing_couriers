import asyncpg
import asyncio
from server_config.config import Settings


class PostgreManager:
    def __init__(self):
        self.host = Settings.DB_HOST
        self.port = Settings.DB_PORT
        self.user = Settings.DB_USER
        self.password = Settings.DB_PASSWORD


    async def get_connect(self):
        return await asyncpg.connect(host=self.host, port=self.port, user=self.user, password=self.password)