from fastapi import APIRouter, Response
from models.courier_model import Courier
from services.courier_manage import CourierManage
from core.urls import url_manage_courier

route_for_couriers = APIRouter()


@route_for_couriers.post(url_manage_courier["CreateCourier"])
async def create_couriers(data: Courier):
    await CourierManage.create_courier(courier=data)
    return Response()


@route_for_couriers.get(url_manage_courier["GetCourier"])
async def get_courier(lng: float, ltd: float):
    return await CourierManage.get_courier(point={'lng': lng, 'ltd': ltd})