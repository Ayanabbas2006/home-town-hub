from fastapi import FastAPI
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, crud, Security
from database.database import get_db, engine
from upload import upload_photo
from database import database
database.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Hometown Hub Api", version="0.0.1")

@app.get("/")
def root():
    return {"message": "Hometown Hub API is running ✅"}
