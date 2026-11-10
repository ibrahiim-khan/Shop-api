from fastapi import FastAPI
from Backend.app.database.database import engine, Base 
from Backend.app.model.product import Product
from Backend.app.router.product import router
app=FastAPI()

Base.metadata.create_all(engine)

app.include_router(router, prefix="/products")


@app.get("/")
def root():
    return {"server is running sucessfully"}