from sqlalchemy import Column , Integer, String, DateTime, Boolean
from Backend.app.database.database import Base

class User(Base):
    __tablename__ = "User"

    user_id= Column(Integer, primary_key=True)
    user_name=Column(String)
    email= Column(String)
    password_hash= Column(String)
    is_active =Column(Boolean, default=True)
    created_at=Column(DateTime)
    role = Column(String)


