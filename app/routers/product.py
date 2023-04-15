from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional

from .. import schemas, database, models


router = APIRouter(
    prefix='/product',
    tags=['Products']
)
get_db = database.get_db


@router.get('/')
def get_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 10,
            is_active: Optional[bool] = None, search: str = None,
             sort_by: str = None, sort_dir: str = 'asc'):
    query = db.query(models.Product)

    if is_active is not None:
        query = query.filter(models.Product.is_active == is_active)

    if search:
            query = query.filter(or_(
                models.Product.name.ilike(f'%{search}%'),
                models.Product.category.ilike(f'%{search}%'),
                models.Product.description.ilike(f'%{search}%')                
            ))

    if sort_by is not None:
        sort_column = getattr(models.Product, sort_by)
        if sort_dir.lower() == 'desc':
            sort_column = sort_column.desc()
        query = query.order_by(sort_column)

    products = query.offset(skip).limit(limit).all()
    return products


@router.get('/{id}', status_code=200)
def get(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with the id {id} is not available")
    return product  


@router.post('/add', status_code=status.HTTP_201_CREATED)
def add(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description,
                                  image_url=request.image_url, category=request.category,
                                    quantity=request.quantity, is_active=request.is_active,
                                      price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with the id {id} is not available")
    db.delete(product)
    db.commit()    
    return f"Product with the id {id} Successfully Deleted"


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with the id {id} is not available")
    product.name = request.name
    product.description = request.description
    product.image_url = request.image_url
    product.category = request.category
    product.quantity = request.quantity
    product.is_active = request.is_active
    product.price = request.price
    db.commit()
    return f"Product with the id {id} Successfully Updated"
