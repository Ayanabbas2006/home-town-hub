from sqlalchemy.engine import create_engine
from sqlalchemy.orm import  relationship, sessionmaker
from Hometown_hub.backend.models.user import User
engine = create_engine('sqlite:///./app.db')



