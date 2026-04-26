from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
 """
 This class represents a table in the database.
 Table name = users
 """
 
 __tablename__ = "users"
 
 # Primary key
 id = Column(Integer, primary_key=True, index=True)
 
 # Username
 username = Column(String, unique=True, index=True)
 
 # Hashed password
 password = Column(String)
 