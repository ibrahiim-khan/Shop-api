from fastapi import APIRouter , status , Depends , HTTPException
from Backend.app.database.database import get_db, engine
from Backend.app.model. user import User 
from Backend.app.schema.user import UserCreate , UserLogin
from Backend.app.utils.security import hash_password , verify_password , createJwt , oauth2_scheme
from sqlalchemy.orm import Session





router=APIRouter()

@router.get("/")
def viewuser(db: Session=Depends(get_db)):
    users=db.query(User).all()
    return users
    


@router.post("/Register",status_code=status.HTTP_201_CREATED)
def register(User_data:UserCreate, db: Session = Depends(get_db)):
    New_user=User(
        user_name=User_data.name,
        email=User_data.email,
        password_hash=hash_password(User_data.password)
    )

    db.add(New_user)
    db.commit()
    db.refresh(New_user)
    return New_user

    

@router.post("/Login")
def login(User_data:UserLogin, db: Session = Depends(get_db)):
    login_detail=db.query(User).filter(User.email==User_data.email).first()

    if not login_detail:
        raise HTTPException (status_code=401, detail="invalid details")

    if not verify_password(User_data.password, login_detail.password_hash):
        raise HTTPException (status_code=401, detail="invalid password or email")

    
    token=createJwt(login_detail.user_id)

    return {
        "token":token,
        "token_type":"bearer"
    }

@router.get("/protected")
def protected_route(token:str=Depends(oauth2_scheme)):
    return {
        "message":"you are authenticated",
        "token":token
    }
    