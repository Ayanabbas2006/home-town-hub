from fastapi import FastAPI
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, crud, Security
from database.database import get_db, engine
from upload import upload_photo
from database import database
from routers.send_mail import *
from fastapi.middleware.cors import CORSMiddleware

database.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hometown Hub Api", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def root():
    return {"message": "Hometown Hub API is running ✅"}

@app.get("/{name}/{email}")
def email(name,email):
    send_otp(name=name,receiver_mail=email)