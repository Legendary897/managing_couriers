import json
from apps.zones.models.zone_model import Zone
from db.db_service import db_client


class ZoneManage:
    @staticmethod
    async def create_zone(zone: Zone):
        name = zone.name_zone
        pre_str = ','.join([f"{i.lng} {i.ltd}" for i in zone.polygon] + [f"{zone.polygon[0].lng} {zone.polygon[0].ltd}"])
        query = f"""
        INSERT INTO zone(name_zone, zone_info)
        VALUES ('{name}',
         st_geomfromtext('POLYGON(({pre_str}))'))
        """
        await db_client.insert_data(query=query)
