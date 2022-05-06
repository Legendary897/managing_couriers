from fastapi import FastAPI
from src.api.v1.zones_routers import route_for_zones
from src.api.v1.couriers_routers import route_for_couriers
from src.db.db_service import init_db


application = FastAPI()
application.include_router(route_for_zones)
application.include_router(route_for_couriers)


@application.on_event("startup")
async def on_startup():
    await init_db()
