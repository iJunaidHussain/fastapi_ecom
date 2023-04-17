from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    description: str
    image_url: str
    category: str
    quantity: int
    is_active: bool
    price: float
    
    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

    class Config():
        orm_mode = True
