from fastapi import Depends
from src.models.zones.zones_models import Zone, ZoneCreate
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_initial import get_session


class ZoneManage:

    @staticmethod
    async def create_zone(zone: ZoneCreate, session: AsyncSession = Depends(get_session)):
        new_zone = Zone(polygon=zone.polygon, name_zone=zone.name_zone)
        session.add(new_zone)
        await session.commit()
        await session.refresh(new_zone)
        return new_zone
