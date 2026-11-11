from fastapi import FastAPI
from Backend.app.database.database import engine, Base 
from Backend.app.model.product import Product
from Backend.app.router.product import router as product_router
from Backend.app.router.user import router as User_router
app=FastAPI()

Base.metadata.create_all(engine)

app.include_router(product_router, prefix="/products")
app.include_router(User_router, prefix="/Users")


@app.get("/")
def root():
    return {"server is running sucessfully"}