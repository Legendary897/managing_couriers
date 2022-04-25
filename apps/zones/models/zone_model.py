from pydantic import BaseModel
from pydantic.fields import List


class Point(BaseModel):
    lng: float
    ltd: float


class Zone(BaseModel):
    polygon: List[Point]
    name_zone: str
