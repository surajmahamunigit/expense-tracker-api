from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite databse URL
DATABASE_URL = "sqlite:///./test.db"

# Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

# Session
SessionLocal = sessionmaker(
 autocommit = False,
 autoflush = False,
 bind = engine
)

# Base
Base = declarative_base()

def get_db():
 """
 This function creates database session and closes it safely
 """
 db = SessionLocal()
 
 try:
  yield db
 finally:
  db.close()
  


