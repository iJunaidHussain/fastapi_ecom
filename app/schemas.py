from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    image_url: str
    category: str
    quantity: int
    is_active: bool
    price: float
    