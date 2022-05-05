from pydantic import BaseModel, fields, types


class CourierInfo(BaseModel):
    first_name: str
    last_name: str
    middle_name: fields.Optional[str]
    phone_number: str
    birthday: types.date


class Courier(BaseModel):
    couriers_info: CourierInfo
    id_zone: int
