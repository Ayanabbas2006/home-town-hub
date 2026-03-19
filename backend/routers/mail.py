from fastapi import APIRouter
from other_modules.send_mail import *
from schemas.otp import send_OTP

router = APIRouter(
    prefix="/register"
)

@router.post('/otp')
def sendEmail(payload: send_OTP):
    send_otp(receiver_mail= payload.email,name=payload.name)