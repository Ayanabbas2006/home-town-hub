from fastapi import APIRouter, Depends, HTTPException, Form
from models.user import User
from typing import Optional
from database.database import get_db
import bcrypt
from schemas.schemas import UserCreate, UserOut
from sqlalchemy.orm import Session

db_router = APIRouter(prefix="/add_user",tags=["Users"])

@db_router.post("/",response_model=UserOut)
def create_user(full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    hometown: str = Form(...),
    photo: Optional[str] = Form(None),
    db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email==email).first()
    if existing:
        raise HTTPException(status_code=400,detail="Email already registered!")
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    new_user = User(
        full_name = full_name,
        email = email,
        hashed_password = hashed_pw,
        photo_url = photo,
        hometown = hometown
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@db_router.get("/{user_id}",response_model=UserOut)
def get_user(user_id:int, db:Session= Depends(get_db)):
    user = db.query(User).filter(User.id== user_id).first()
    if not user:
        raise  HTTPException(status_code=404, detail="User not found!")
    return user
