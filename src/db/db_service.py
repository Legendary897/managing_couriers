import asyncpg
from core.config import Settings


class PostgreManager:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostgreManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.host = Settings.DB_HOST
        self.port = Settings.DB_PORT
        self.user = Settings.DB_USER
        self.password = Settings.DB_PASSWORD
        self.db = Settings.DATABASE
        self.pool = None

    async def setting_pools(self):
        self.pool = await asyncpg.create_pool

    async def fetchall(self, query):
        async with await asyncpg.create_pool(host=self.host,
                                             port=self.port,
                                             user=self.user,
                                             password=self.password,
                                             database=self.db) as pool:
            return await pool.fetch(query)

    async def insert_data(self, query):
        async with await asyncpg.create_pool(host=self.host,
                                             port=self.port,
                                             user=self.user,
                                             password=self.password,
                                             database=self.db) as pool:
            await pool.execute(query)


db_client = PostgreManager()
