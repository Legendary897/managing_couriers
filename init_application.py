from fastapi import FastAPI
from routers.zones_routers import route_for_zones
from routers.couriers_routers import route_for_couriers


application = FastAPI()
application.include_router(route_for_zones)
application.include_router(route_for_couriers)
