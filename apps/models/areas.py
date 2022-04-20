from pydantic import BaseModel
from pydantic.fields import List


class Point(BaseModel):
    lng: float
    ltd: float


class Area(BaseModel):
    polygon: List[Point]
