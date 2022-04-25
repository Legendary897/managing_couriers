from pydantic import BaseModel


class CourierInfo(BaseModel):
    name: str
    surname: str
    age: int


class Courier(BaseModel):
    couriers_info: CourierInfo
    id_zone: int
