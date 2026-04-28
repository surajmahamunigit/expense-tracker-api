from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User

SECURITY_KEY = "mysecretkey"
ALGORITHM = "HS256"

security = HTTPBearer()


def get_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return credentials.credentials


def get_current_user(token: str = Depends(get_token), db: Session = Depends(get_db)):
    try:
        # Take the JWT token and extract the uername
        payload = jwt.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate token")

    # Find the user in the db
    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user
