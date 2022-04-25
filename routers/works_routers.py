from fastapi import APIRouter, Response
from server_config.urls import url_manage_cour
from apps.zones.models.zone_model import Zone
from apps.zones.services.zone_manage import ZoneManage
from apps.couriers.models.courier_model import Courier
from apps.couriers.services.courier_manage import CourierManage

route_for_couriers = APIRouter()


@route_for_couriers.post(url_manage_cour["CreateZone"])
async def create_zone_of_delivery(data: Zone):
    await ZoneManage.create_zone(zone=data)
    return Response()


@route_for_couriers.post(url_manage_cour["CreateCourier"])
async def create_couriers(data: Courier):
    await CourierManage.create_courier(courier=data)
    return Response()


@route_for_couriers.get(url_manage_cour["GetCourier"])
async def get_courier(lng: float, ltd: float):
    return await CourierManage.get_courier(point={'lng': lng, 'ltd': ltd})
