from json import loads


async def get_courier_info(data: dict):
    return {
        "id": data["id"],
        "id_area": data["id_area"],
        "couriers_info": loads(data["couriers_info"])
    }