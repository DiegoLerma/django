from ninja import Schema


class ItemSchema(Schema):
    id: int
    name: str
    description: str


class ItemCreateSchema(Schema):
    name: str
    description: str
