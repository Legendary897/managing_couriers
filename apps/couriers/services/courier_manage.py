import json
from apps.couriers.serialize.serialize_couriers import get_courier_info
from apps.couriers.models.courier_model import Courier
from db.db_service import db_client


class CourierManage:

    @staticmethod
    async def get_courier(point: dict):
        query_check = f"""
        SELECT c.id AS id_cour, c.couriers_info AS info, z.name_zone AS zone_name, z.id AS zone_id 
        FROM couriers c
        JOIN "zone" z ON z.id = c.id_zone 
        WHERE z.id IN (
            SELECT id 
            FROM "zone"  
            WHERE ST_Contains(zone_info, ST_Point({point['lng']}, {point['ltd']}))
        )"""
        results = list(await db_client.fetchall(query=query_check))
        if len(results) > 0:
            return await get_courier_info(results[0])
        return {"info": "Точка доставки не входит ни в одну из доступных зон доставки"}

    @staticmethod
    async def create_courier(courier: Courier):
        id_zone = courier.id_zone
        courier_info = courier.couriers_info.json()
        await db_client.insert_data(
            query=f"""INSERT INTO couriers(id_zone, couriers_info) VALUES ({id_zone}, '{courier_info}')"""
        )
