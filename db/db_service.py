import asyncpg
from server_config.config import Settings


class PostgreManager:
    def __init__(self):
        self.host = Settings.DB_HOST
        self.port = Settings.DB_PORT
        self.user = Settings.DB_USER
        self.password = Settings.DB_PASSWORD
        self.db = Settings.DATABASE
        self.pool = None

    async def setting_pools(self):
        self.pool = await asyncpg.create_pool(host=self.host,
                                              port=self.port,
                                              user=self.user,
                                              password=self.password,
                                              database=self.db)

    async def fetchall(self, query):
        if self.pool is None:
            await self.setting_pools()
        return await self.pool.fetch(query)

    async def insert_data(self, query):
        if self.pool is None:
            await self.setting_pools()
        await self.pool.execute(query)


db_client = PostgreManager()
