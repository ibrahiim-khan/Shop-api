import os
from dotenv import load_dotenv
from passlib.context import  CryptContext 
from datetime import datetime, timedelta, timezone  
from Backend.app.database.database import get_db
from Backend.app.model.user import User
from fastapi import Depends , HTTPException
from sqlalchemy.orm import Session
from jose import jwt

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
oauth2_scheme=HTTPBearer(   )

#this code is used for password hashing and hashed password is store in the database

pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password:str):
    return pwd_context.hash(password)

#verify_password function used to verify the password provided at login time and stored in the database while register

def verify_password(plain_password: str, hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)



# jwt  token genrate karna ke liya code likh raha hu 

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")

ALGORITHM  = "HS256"
 
def createJwt(user_id:int):
    expire=datetime.now(timezone.utc)+timedelta(seconds=40)
    payload={
        "sub":str(user_id),
        "exp":expire
    }

    token=jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



#token ko decode karna verify karna (jab client sai vapas aayga)

def verifytoken(token:str):
    try :
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except Exception as e:
        print("Jwt",e)
        return None


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme),db:Session =Depends(get_db)):
    token = credentials.credentials
    payload=verifytoken(token)

    if not payload:
        raise HTTPException(status_code=401, detail="invalid token")
    
    user_id=payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401, detail="invalid token")

    object_user=db.query(User).filter(User.User_id==int (user_id)).first()

    if not object_user :
        raise HTTPException(status_code=404 , detail="User not found ")



    return object_user
