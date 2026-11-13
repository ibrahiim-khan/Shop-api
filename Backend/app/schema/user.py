from pydantic import  BaseModel,EmailStr , Field

class UserCreate(BaseModel):
    name:str=Field(max_length=100)
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name:str=Feild(max_length=100)
    email:EmailStr
    is_active=bool