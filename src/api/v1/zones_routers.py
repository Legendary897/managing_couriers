from fastapi import APIRouter, Response
from src.core.urls import url_manage_zone
from src.models.zones.zones_models import ZoneCreate
from src.services.zones.zone_manage import ZoneManage

route_for_zones = APIRouter()


@route_for_zones.post(url_manage_zone["CreateZone"])
async def create_zone_of_delivery(data: ZoneCreate):
    await ZoneManage.create_zone(zone=data)
    return Response()
