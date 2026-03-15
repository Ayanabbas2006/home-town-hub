from fastapi import FastAPI
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, crud, Security
from database.database import get_db, engine
from cloudinary import upload_photo

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Hometown Hub Api", version="0.0.1")

app.get("/")
def root():
    return {"msg":"Api is live"}