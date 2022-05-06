from typing import List

from sqlalchemy import Column
from sqlmodel import SQLModel, Field, JSON


class Point(SQLModel):
    lng: float
    ltd: float


class ZonesBaseModel(SQLModel):
    polygon: List[Point] = Field(sa_column=Column(JSON))
    name_zone: str

    class Config:
        arbitrary_types_allowed = True


class Zone(ZonesBaseModel, table=True):
    id: int = Field(default=None, primary_key=True)


class ZoneCreateModel(ZonesBaseModel):
    pass
