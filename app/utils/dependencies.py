from fastapi import FastAPI, HTTPException, Depends
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY= "mysecretkey"
ALGORITHM= "HS256"

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str= Depends(oauth2_scheme)):
 try:
  payload= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  username= payload.get("sub")

  if not username:
   raise HTTPException(status_code=401, detail="Invalid token")
  
  return username
 except JWTError:
  raise HTTPException(status_code=401, detail="Invalid token")
