from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from database.database import get_db
import bcrypt
from schemas.schemas import UserCreate, UserOut
from sqlalchemy.orm import Session

db_router = APIRouter(prefix="/add_user",tags=["Users"])

@db_router.post("/",response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email==user.email).first()
    if existing:
        raise HTTPException(status_code=400,detail="Email already registered!")
    hashed_pw = bcrypt.hashpw(user.password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    new_user = User(
        full_name = user.full_name,
        email = user.email,
        hashed_password = hashed_pw,
        photo_url = user.photo_url,
        hometown = user.hometown
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
