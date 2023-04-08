from fastapi import FastAPI

from app.database import engine, Base
from app.routers import product


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(product.router)


# Test root directory
@app.get('/')
def root():
    return "Hello World"


# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn main:app --reload