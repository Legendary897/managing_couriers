from pydantic import BaseModel
from pydantic.fields import List, Field


class Point(BaseModel):
    lng: float
    ltd: float


class Zone(BaseModel):
    polygon: List[Point] = Field(min_items=3)
    name_zone: str
