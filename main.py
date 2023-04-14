from fastapi import FastAPI
import uvicorn

from app.database import engine, Base
from app.routers import product


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(product.router)


# Test root directory
@app.get('/')
def root():
    return "FastAPI Connection Successfuly Stablished"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
