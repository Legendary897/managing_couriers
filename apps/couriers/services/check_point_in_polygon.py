from shapely.geometry import Point, Polygon


async def check_in(point: dict, polygon: list):
    return Point([point['lng'], point['ltd']]).within(Polygon(polygon))
