from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    is_active = Column(Boolean)
    price = Column(Float)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean)
