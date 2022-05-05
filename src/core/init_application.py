from fastapi import FastAPI
from api.v1.zones_routers import route_for_zones
from api.v1.couriers_routers import route_for_couriers
from db.db_initial import init_db


application = FastAPI()
application.include_router(route_for_zones)
application.include_router(route_for_couriers)


@application.on_event("startup")
async def on_startup():
    await init_db()
