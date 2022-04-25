from fastapi import FastAPI
from cashews import cache
from server_config.config import Settings
from routers.zones_routers import route_for_zones
from routers.couriers_routers import route_for_couriers


cache.setup(Settings.REDIS_HOST,
            db=Settings.REDIS_ZONE_INFO_DB,
            port=Settings.REDIS_PORT,
            wait_for_connection_timeout=0.5,
            safe=False,
            hash_key=Settings.CACHE_ZONE_KEY,
            enable=True)


application = FastAPI()
application.include_router(route_for_zones)
application.include_router(route_for_couriers)
