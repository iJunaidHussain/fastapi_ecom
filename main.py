from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import schemas, models


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get('/')
def index():
    return "Hello World"


@app.post('/products')
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product("ab", "cd", "ef", "gh", 23, True, 55.6)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn main:app --reload