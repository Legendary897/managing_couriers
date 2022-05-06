from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_service import get_session
from src.models.couriers.couriers_models import CourierCreateModel
from src.services.couriers.courier_manage import CourierManage
from src.core.urls import url_manage_courier

route_for_couriers = APIRouter()


@route_for_couriers.post(url_manage_courier["CreateCourier"])
async def create_couriers(data: CourierCreateModel, session: AsyncSession = Depends(get_session)):
    await CourierManage.create_courier(courier=data, session=session)
    return Response()


@route_for_couriers.get(url_manage_courier["GetCourier"])
async def get_courier(lng: float, ltd: float, session: AsyncSession = Depends(get_session)):
    return await CourierManage.get_courier(point={'lng': lng, 'ltd': ltd}, session=session)