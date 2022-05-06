from typing import List

from sqlalchemy import Column
from sqlmodel import SQLModel, Field, JSON


class Point(SQLModel):
    lng: float
    ltd: float


class ZonesBaseModel(SQLModel):
    name_zone: str


class Zone(ZonesBaseModel, table=True):
    id: int = Field(default=None, primary_key=True)
    polygon: dict = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True


class ZoneCreateModel(ZonesBaseModel):
    polygon: List[Point] = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True
