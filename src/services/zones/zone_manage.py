from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.zones.zones_models import Zone, ZoneCreateModel


class ZoneManage:

    @staticmethod
    async def create_zone(zone: ZoneCreateModel, session: AsyncSession):
        new_zone = Zone(polygon=zone.polygon, name_zone=zone.name_zone)
        session.add(new_zone)
        try:
            await session.commit()
            await session.refresh(new_zone)
            return new_zone
        except IntegrityError as _:
            await session.rollback()

