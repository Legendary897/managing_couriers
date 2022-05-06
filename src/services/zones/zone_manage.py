from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.zones.zones_models import Zone, ZoneCreateModel


class ZoneManage:

    @staticmethod
    async def create_zone(zone: ZoneCreateModel, session: AsyncSession):
        polygon = {
            'data': []
        }
        for point in zone.polygon:
            buf_data = {}
            for key, val in point:
                buf_data[key] = val
            polygon['data'].append(buf_data)
        new_zone = Zone(polygon=polygon, name_zone=zone.name_zone)
        session.add(new_zone)
        try:
            await session.commit()
            await session.refresh(new_zone)
            return new_zone
        except IntegrityError as _:
            await session.rollback()

