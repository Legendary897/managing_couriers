from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.urls import url_manage_zone
from db.db_service import get_session
from models.zones.zones_models import ZoneCreateModel
from services.zones.zone_manage import ZoneManage

route_for_zones = APIRouter()


@route_for_zones.post(url_manage_zone["CreateZone"])
async def create_zone_of_delivery(data: ZoneCreateModel, session: AsyncSession = Depends(get_session)):
    await ZoneManage.create_zone(zone=data, session=session)
    return Response()
