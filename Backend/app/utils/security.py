import os
from dotenv import load_dotenv
from passlib.context import  CryptContext 
from jose import jwt

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="User/Login")

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
    payload={
        "sub":str(user_id)
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


def get_current_user(token:str=Depends(oauth2_scheme)):
    payload=verifytoken(token)

    if not payload:
        raise Exception("invalid token")
    
    user_id=payload.get("sub")

    if not user_id:
        raise Exception("invalid token")

    
    return user_id
