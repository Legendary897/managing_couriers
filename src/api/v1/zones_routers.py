from fastapi import APIRouter, Response
from core.urls import url_manage_zone
from models.zone_model import Zone
from services.zone_manage import ZoneManage

route_for_zones = APIRouter()


@route_for_zones.post(url_manage_zone["CreateZone"])
async def create_zone_of_delivery(data: Zone):
    await ZoneManage.create_zone(zone=data)
    return Response()
