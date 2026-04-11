from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    hometown: str
    password: str
    photo_url: Optional[str] = None
    account_type: str
    gender: str
    user_name: str

class UserOut(BaseModel):
    Id: int
    full_name: str
    email: str
    created_at: datetime
    photo_url: Optional[str] = None
    account_type: str
    gender: str
    user_name: str

    class config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
