from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.urls import url_manage_zone
from src.db.db_service import get_session
from src.models.zones.zones_models import ZoneCreateModel
from src.services.zones.zone_manage import ZoneManage

route_for_zones = APIRouter()


@route_for_zones.post(url_manage_zone["CreateZone"])
async def create_zone_of_delivery(data: ZoneCreateModel, session: AsyncSession = Depends(get_session)):
    await ZoneManage.create_zone(zone=data, session=session)
    return Response()
