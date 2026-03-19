from fastapi import APIRouter
from other_modules.send_mail import *

router = APIRouter(
    prefix="/register"
)

@router.post('/otp')
def sendEmail(payload):
    send_otp(receiver_mail= payload.email,name=payload.name)