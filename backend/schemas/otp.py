from pydantic import BaseModel, EmailStr

class send_OTP:
    name: str
    email: EmailStr