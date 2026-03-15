from sqlalchemy import create_engine
from sqlalchemy.orm import  relationship, sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL","postgresql://users_rqg9_user:jd56dC5h4BrD2UMX3XFUAWbOZQaB9CSX@dpg-d6rftp14tr6s7388plg0-a/users_rqg9")

engine = create_engine(DATABASE_URL,connect_args={})
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
