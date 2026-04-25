from pydantic import BaseModel

class LoginRequest(BaseModel):
 username: str
 password: str
 
class UserAuth(BaseModel):
 username: str
 password: str