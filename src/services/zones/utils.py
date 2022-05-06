from shapely.geometry import Polygon, Point


async def cross_poly_point(pre_data, point):
    for zone in pre_data:
        if Point((point['lng'], point['ltd'])).within(Polygon((i['lng'], i['ltd']) for i in zone.polygon['data'])):
            return zone.id
    return -1
