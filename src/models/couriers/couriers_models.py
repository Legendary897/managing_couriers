from typing import Optional
from datetime import date

from sqlalchemy import Column
from sqlmodel import SQLModel, Field, JSON


class CourierInfo(SQLModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = Field(default=None)
    phone_number: str
    birthday: date


class CourierBaseModel(SQLModel):
    couriers_info: CourierInfo = Field(sa_column=Column(JSON))
    id_zone: Optional[int] = Field(foreign_key="zone.id")

    class Config:
        arbitrary_types_allowed = True


class Courier(CourierBaseModel, table=True):
    id: int = Field(default=None, primary_key=True)


class CourierCreateModel(CourierBaseModel):
    pass
