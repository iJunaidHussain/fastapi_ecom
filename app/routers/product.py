from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, database, models


router = APIRouter(
    prefix='/product',
    tags=['Products']
)
get_db = database.get_db


@router.post('/add', status_code=status.HTTP_201_CREATED)
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description,
                                  image_url=request.image_url, category=request.category,
                                    quantity=request.quantity, is_active=request.is_active,
                                      price=request.price)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product