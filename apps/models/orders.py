from pydantic import BaseModel


class Order(BaseModel):
    operator_id: str
    order_id: str
    status: int