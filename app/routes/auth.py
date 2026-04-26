from typing import Optional
from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.schemas.auth import LoginRequest, UserAuth 

router= APIRouter()

# Fake db
fake_users_db= {}

# Configure the JWT
SECURITY_KEY= "mysecretkey"
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE_TIME= 30 

pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


# Create access token
def create_access_token(data: dict):
    to_encode= data.copy()
    expire= datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)

    to_encode.update({"exp": expire})

    encoded_jwt= jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)

    return encoded_jwt



@router.post("/register")
def register(data: UserAuth):
    username= data.username
    password= data.password

    if username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exist")
    
    hashed_password= hash_password(password)
    
    fake_users_db[username]= {"username": username, "password":hashed_password}
    
    return {"message": "User registered"}



@router.post("/login")
def login(data: LoginRequest):

    username = data.username
    password = data.password


    user = fake_users_db.get(username)

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    hashed_password = user.get("password")

    if not hashed_password:
        raise HTTPException(status_code=500, detail="Password not found in DB")

    if not verify_password(password, hashed_password):
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = create_access_token(data={"sub": username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }