from datetime import timedelta
import json
from cashews import cache
from apps.zones.models.zone_model import Zone
from db.db_service import db_client


class ZoneManage:
    @staticmethod
    async def create_zone(zone: Zone):
        name = zone.name_zone
        info = json.dumps({
            "polygon": [[i.lng, i.ltd] for i in zone.polygon]
        })
        query = f"""
        INSERT INTO area(name_zone, area_info)
        VALUES ('{name}', '{info}')
        """
        await db_client.insert_data(query=query)
        await cache.delete(key="zones")

    @staticmethod
    @cache(ttl=timedelta(days=1), key="zones")
    async def get_all_zone():
        results = [{
            "id": i['id'],
            "area_info" : i['area_info']
        } for i in await db_client.fetchall(query="SELECT id, area_info FROM area")]
        return results