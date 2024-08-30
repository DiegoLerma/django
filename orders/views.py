from typing import List

from ninja import Router
from orders.models import Order
from orders.schemas import OrderSchema, OrderCreateSchema
from django.shortcuts import get_object_or_404

router = Router()


@router.get("/orders", response=List[OrderSchema])
def list_orders(request):
    return Order.objects.all()


@router.get("/orders/{order_id}", response=OrderSchema)
def get_order(request, order_id: int):
    return get_object_or_404(Order, id=order_id)


@router.post("/orders", response=OrderSchema)
def create_order(request, payload: OrderCreateSchema):
    order = Order.objects.create(**payload.dict())
    return order


@router.put("/orders/{order_id}", response=OrderSchema)
def update_order(request, order_id: int, payload: OrderCreateSchema):
    order = get_object_or_404(Order, id=order_id)
    for attr, value in payload.dict().items():
        setattr(order, attr, value)
    order.save()
    return order


@router.delete("/orders/{order_id}", response={204: None})
def delete_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return 204, None
