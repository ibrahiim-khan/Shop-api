from fastapi import FastAPI 
import json
app=FastAPI()

def load_data():
    with open ('database.json','r') as f:
        data=json.dump(f)
        return data


@app.get("/products")
def view_products ():
    data=load_data()
    return data


@app.get("/products/{product_id}")
def view_particular_product( product_id):
    data=load_data()
    if product_id not in data:
        raise HTTPException(status_code=404,detail="Product NOT Found!")

    details=data.get(product_id)
    return details


@app.get("/products")
def filtering(sortby:str=Path(...,description="YOU CAN SORT IT BASED ON CATEGORY or BRAND",example="Electronics")):
    data=load_data()
    sortedby=['id','category','price','brand','stocks']
    if sortby not in sortedby:
        raise HTTPException(status_code=422,detail="Wrong input!")

    sorted=sorted(data.value(),key=lambda x:x.get(sortby,0),reverse=True)
    return sorted


@app.post("/create")
def create(product:PRODUCT)