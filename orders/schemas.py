from ninja import Schema
from datetime import datetime


class OrderSchema(Schema):
    id: int
    product_name: str
    quantity: int
    price: float
    created_at: datetime


class OrderCreateSchema(Schema):
    product_name: str
    quantity: int
    price: float
