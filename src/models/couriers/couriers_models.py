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
    id_zone: Optional[int] = Field(foreign_key="zone.id")


class Courier(CourierBaseModel, table=True):
    id: int = Field(default=None, primary_key=True)
    couriers_info: dict = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True


class CourierCreateModel(CourierBaseModel):
    couriers_info: CourierInfo = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True
