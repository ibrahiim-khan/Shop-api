from sqlalchemy import Column ,Integer, String, Float
from Backend.app.database.database import Base


class Product(Base):
    __tablename__= "products"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    description=Column(String)
    stock=Column(Integer)
    price=Column(Float)