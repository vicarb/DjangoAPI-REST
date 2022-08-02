from ninja import Schema

class NegocioSchema(Schema):
    category_id: int
    id: int
    title: str
    negocio_slug: str
    description: str

class NotFoundSchema(Schema):
    message: str
