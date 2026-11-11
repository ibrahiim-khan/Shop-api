from fastapi import APIRouter,Depends , HTTPException, status
from Backend.app.database.database import get_db
from Backend.app.schema.product import ProductCreate , UpdateProduct
from Backend.app.model.product import Product
from sqlalchemy.orm import Session




router=APIRouter()
#creating routes


@router.get("/")
def viewproducts(db: Session = Depends(get_db)):
    products=db.query(Product).all()
    return products


@router.get("/{Product_id}")
def viewproduct(Product_id:int, db :Session = Depends(get_db)):
    product=db.query(Product).filter(Product.id== Product_id).first()

    if not product:
        raise HTTPException(status_code=404,detail="Not found")

    return product

@router.post("/",status_code=status.HTTP_201_CREATED)
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



@router.delete("/{Product_id}")
def deleteProduct(Product_id:int,db : Session = Depends(get_db)):
    product=db.query(Product).filter(Product.id==Product_id).first()

    if not product:
        raise HTTPExceptin ( status_code=404, detail="Not found")

    db.delete(product)
    db.commit()

    return {"Message":"Product delete Permanently"}

@router.put("/{Product_id}")
def updateProduct(Product_id: int, Product_data : UpdateProduct ,db: Session = Depends(get_db)):
    product=db.query(Product).filter(Product.id==Product_id).first()

    if not product:
        raise HTTPException(status_code=404 , detail="Not found")
    
    name= Product_data.name
    description=Product_data.description
    stock=Product_data.stock
    price=Product_data.price

    db.commit()
    db.refresh(product)
    return {"message": "Product updated successfully ",
        "product":product}






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
