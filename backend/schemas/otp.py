from pydantic import BaseModel, EmailStr

class send_OTP(BaseModel):
    name: str
    email: EmailStr

class user_OTP(BaseModel):
    otp: int