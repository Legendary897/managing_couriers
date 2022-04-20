from fastapi import FastAPI
from routers.works_routers import route_for_couriers

application = FastAPI()
application.include_router(route_for_couriers)
