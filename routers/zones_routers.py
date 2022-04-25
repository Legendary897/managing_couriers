from fastapi import APIRouter, Response
from server_config.urls import url_manage_zone
from apps.zones.models.zone_model import Zone
from apps.zones.services.zone_manage import ZoneManage

route_for_zones = APIRouter()


@route_for_zones.post(url_manage_zone["CreateZone"])
async def create_zone_of_delivery(data: Zone):
    await ZoneManage.create_zone(zone=data)
    return Response()
