import json
from apps.couriers.serialize.serialize_couriers import get_courier_info
from apps.couriers.services.check_point_in_polygon import check_in
from apps.couriers.models.courier_model import Courier
from apps.zones.services.zone_manage import ZoneManage
from db.db_service import db_client


class CourierManage:

    @staticmethod
    async def get_courier(point: dict):
        areas = await ZoneManage.get_all_zone()
        for area in areas:
            if await check_in(point=point, polygon=json.loads(area['zone_info'])['polygon']):
                results = list(await db_client.fetchall(
                    query=f"""SELECT id, couriers_info, id_zone FROM couriers WHERE id_zone = {area['id']}"""))
                return await get_courier_info(results[0]) if len(results) > 0 else {"info": "В данной зоне доставки нет курьеров"}
        return {"info": "Точка доставки не входит ни в одну из доступных зон доставки"}

    @staticmethod
    async def create_courier(courier: Courier):
        id_zone = courier.id_zone
        courier_info = courier.couriers_info.json()
        await db_client.insert_data(
            query=f"""INSERT INTO couriers(id_zone, couriers_info) VALUES ({id_zone}, '{courier_info}')"""
        )
