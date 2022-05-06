from json import loads

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.couriers.serializers.serialize_couriers import get_courier_info
from models.couriers.couriers_models import Courier, CourierCreate
from models.zones.zones_models import Zone
from db.db_initial import get_session
from services.zones.utils import cross_poly_point


class CourierManage:

    @staticmethod
    async def get_courier(point: dict, session: AsyncSession = Depends(get_session)):
        pre_data = await session.execute(statement=select(Zone))
        if zone_id := (await cross_poly_point(pre_data=pre_data, point=point)) != -1:
            statement_courier = select(Courier, Zone).where(Courier.id_zone == Zone.id, Zone.id == zone_id)
            results = await session.execute(statement=statement_courier)
            return [{"id": courier.id,
                    "id_zone": zone.id,
                    "name_zone": zone.name_zone,
                    "couriers_info": loads(courier.couriers_info)
                     } for courier, zone in results]
        return {"info": "Точка доставки не входит ни в одну из доступных зон доставки"}

    @staticmethod
    async def create_courier(courier: CourierCreate, session: AsyncSession = Depends(get_session)):
        new_courier = Courier(couriers_info=courier.couriers_info, id_zone=courier.id_zone)
        session.add(new_courier)
        await session.commit()
        await session.refresh(new_courier)
        return new_courier
