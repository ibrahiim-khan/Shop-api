from fastapi import APIRouter , status , Depends , HTTPException
from Backend.app.database.database import get_db, engine
from Backend.app.model. user import User 
from Backend.app.schema.user import UserCreate , UserLogin , UserUpdate
from Backend.app.utils.security import hash_password , verify_password , createJwt , get_current_user ,require_admin , object_level_authk
from sqlalchemy.orm import Session





router=APIRouter()


@router.post("/Register",status_code=status.HTTP_201_CREATED)
def register(User_data:UserCreate, db: Session = Depends(get_db)):
    New_user=User(
        user_name=User_data.name,
        email=User_data.email,
        password_hash=hash_password(User_data.password),
        role="User"
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


@router.get("/ALL_Users")
def viewuser(db: Session=Depends(get_db),user:User=Depends(require_admin)):
    users=db.query(User).all()
    return users
    



@router.get("/Admin")
def admin(user:User=Depends(require_admin)):
    return {
        "message":"Welcome Admin",
        "Name":user.user_name,
        "email":user.email,
        "role":user.role
    }


@router.put("/Update_profie/{user_id}")
def update_profile(user_detail:UserUpdate,db:Session=Depends(get_db),authorized_user_id:int=Depends(object_level_auth)):
    























# @router.get("/protected")
# def protected_route(user: User = Depends(get_current_user)):
#     if (User.role !="admin"):
#         raise HTTPException(
#             status_code=403,
#             detail="Authenticated But NOt autharized"
#         )

#     return {
#         "message": "You are authenticated",
#         "user_id": user.user_id,
#         "user_name":user.user_name,
#         "user_email":user.email,
#         }
    }