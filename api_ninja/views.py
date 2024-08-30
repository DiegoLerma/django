from ninja import Router
from .models import Item
from .schemas import ItemSchema, ItemCreateSchema
from django.shortcuts import get_object_or_404

router = Router()


@router.get("/items", response=list[ItemSchema])
def list_items(request):
    return list(Item.objects.all())


@router.get("/items/{item_id}", response=ItemSchema)
def get_item(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)
    return item


@router.post("/items", response=ItemSchema)
def create_item(request, data: ItemCreateSchema):
    item = Item.objects.create(**data.dict())
    return item


@router.put("/items/{item_id}", response=ItemSchema)
def update_item(request, item_id: int, data: ItemCreateSchema):
    item = get_object_or_404(Item, id=item_id)
    for attr, value in data.dict().items():
        setattr(item, attr, value)
    item.save()
    return item


@router.delete("/items/{item_id}", response=dict)
def delete_item(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return {"success": True}
