from fastapi import APIRouter, HTTPException, Header, Response
from server_config.urls import url_manage_cour
from apps.models.areas import Area
from apps.models.orders import Order

route_for_couriers = APIRouter()


@route_for_couriers.post(url_manage_cour["CreateZone"])
async def create_zone_of_delivery(data: Area):
    return Response()


@route_for_couriers.post(url_manage_cour["ManageOrder"])
async def accept_the_order(data: Order):
    return Response()


@route_for_couriers.put(url_manage_cour["ManageOrder"])
async def update_the_order(data: Order):
    return Response()


@route_for_couriers.delete(url_manage_cour["ManageOrder"])
async def delete_the_order(order_id):
    return Response()


@route_for_couriers.get(url_manage_cour["GetCourier"])
async def get_courier(lng: float, ltd: float):
    return Response()
