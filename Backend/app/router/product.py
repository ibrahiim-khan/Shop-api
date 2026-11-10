from fastapi import APIRouter,Depends
from Backend.app.database.database import get_db
from Backend.app.schema.product import ProductCreate
from Backend.app.model.product import Product
from sqlalchemy.orm import Session




router=APIRouter()
#creating routes


@router.get("/")
def viewproducts(db: Session = Depends(get_db)):
    products=db.query(Product).all()
    return products




@router.post("/")
def createProduct(product:ProductCreate,db:Session=Depends(get_db)):
    new_product=Product(
        name=product.name,
        description=product.description,
        stock=product.stock,
        price=product.price,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product











# @router.get("PRODUCTS/{product_id}")
# def product(int product_id ):
#     pass



# @router.post("PRODUCTS")
# def new_product():
#     pass



# @router.put("PRODUCTS/{product_id}")
# def updateproduct(int product_id):
#     pass


# @router.delete("PRODUCTS/{product_id}")
# def deleteproduct(int product_id):
#     pass
