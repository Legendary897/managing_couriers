from json import loads


async def get_courier_info(data: dict):
    return {
        "id": data["id_cour"],
        "id_zone": data["zone_id"],
        "name_zone": data["zone_name"],
        "couriers_info": loads(data["info"])

    }
