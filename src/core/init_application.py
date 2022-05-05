from fastapi import FastAPI
from api.v1.zones_routers import route_for_zones
from api.v1.couriers_routers import route_for_couriers


application = FastAPI()
application.include_router(route_for_zones)
application.include_router(route_for_couriers)
