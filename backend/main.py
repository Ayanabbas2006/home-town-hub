from fastapi import FastAPI
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, crud, Security
from database.database import get_db, engine
from backend.routers.upload import upload_router
from database import database
from routers.mail import *
from fastapi.middleware.cors import CORSMiddleware

database.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hometown Hub Api", version="0.0.1")
app.include_router(router=[router,upload_router])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hometownhub.vercel.app","http:localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Hometown Hub API is running ✅"}

