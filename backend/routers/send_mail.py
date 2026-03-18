import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random
from dotenv import load_dotenv

load_dotenv()

def generate_otp():
    return random.randint(111111,999999)

def send_otp(name,receiver_mail):
    otp=generate_otp()
    message = Mail(
        from_email='mojisshuja@gmail.com',
        to_emails=receiver_mail,
        subject='Thanks for registering at HomeTownHub',
        html_content=f"""
        <h1> HomeTownHub</h1>
        Dear {name},
        <div>
        We are pleased by your presence, here is your 6-digit secret code.
        kindly DO NOT SHARE IT WITH ANYONE!
        <div>
        <h4>OTP: {otp}</h4>
        </div>
        </div>
        Thanks,<br>
        Team<br>
        HomeTownHub
        """
    )

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message=message)
        return (response.status_code)
    except Exception  as error:
        return (error)