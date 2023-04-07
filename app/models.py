from sqlalchemy import Column, Integer, String, Float, Boolean


class Product():
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    price = Column(Float)
