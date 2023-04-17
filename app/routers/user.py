from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, database, models


router = APIRouter(
    prefix='/user',
    tags=['User']
)
get_db = database.get_db


@router.get('/{id}', response_model=schemas.User)
def get(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


@router.post('/', response_model=schemas.User)
def add(request: schemas.User, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(
        models.User.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='Username already exists')
    existing_email = db.query(models.User).filter(
        models.User.email == request.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail='Email already exists')

    new_user = models.User(username=request.username, password=request.password, 
                           email=request.email, full_name=request.full_name,
                           disabled=request.disabled)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()
    return 'User with the id {id} Successfully Deleted'
 