import json

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
