from pydantic import BaseModel , Field 
from typing import Annotated 
#  List , Dict , Optional

class ProductCreate(BaseModel):
    name: Annotated[str , Field(max_length=50 , title= "Name of the Product", description="Give the name of the product")]
    description : Annotated[str, Field( max_length=50, title="Give description of product")]
    stock: int = Field(gt=0)
    price : float = Field (gt=0)

class UpdateProduct(BaseModel):
    name: str
    description : str =Field(max_length=50)
    stock: int = Field(gt=0)
    price : float = Field (gt=0)

