from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db_service import get_session
from models.couriers.couriers_models import CourierCreateModel
from services.couriers.courier_manage import CourierManage
from core.urls import url_manage_courier

route_for_couriers = APIRouter()


@route_for_couriers.post(url_manage_courier["CreateCourier"])
async def create_couriers(data: CourierCreateModel, session: AsyncSession = Depends(get_session)):
    await CourierManage.create_courier(courier=data, session=session)
    return Response()


@route_for_couriers.get(url_manage_courier["GetCourier"])
async def get_courier(lng: float, ltd: float, session: AsyncSession = Depends(get_session)):
    return await CourierManage.get_courier(point={'lng': lng, 'ltd': ltd}, session=session)