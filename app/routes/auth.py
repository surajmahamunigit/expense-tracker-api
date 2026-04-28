from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.schemas.auth import LoginRequest, UserAuth
from sqlalchemy.orm import Session
from app.models.user import User
from app.db.database import get_db

router = APIRouter()


# Configure the JWT
SECURITY_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


# Create access token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@router.post("/register")
def register(data: UserAuth, db: Session = Depends(get_db)):
    username = data.username
    password = data.password

    # Check if user exist in db
    existing_user = db.query(User).filter(User.username == username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exist")

    hashed_password = hash_password(password)

    new_user = User(username=username, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered"}


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    username = data.username
    password = data.password

    # existing user in dbuser
    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    access_token = create_access_token(data={"sub": username})

    return {"access_token": access_token, "token_type": "bearer"}
