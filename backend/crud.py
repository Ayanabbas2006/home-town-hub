from sqlalchemy.orm import Session
from models.user import User
from schemas.schemas import UserCreate
import Security.auth

def get_user_by_email(db:Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session,user_id: int):
    return db.query(User.user).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    new_user = User(
        full_name = user.full_name,
        email = user.email,
        hashed_password = Security.auth.hashed_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_photo_url(db: Session, user_id: int, photo_url:str):
    user = get_user_by_id(db, user_id)
    user.photo_url = photo_url
    db.commit()
    db.refresh(user)
    return user