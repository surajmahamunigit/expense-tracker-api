from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    username: str
    password: str = Field(..., max_length=72)


class UserAuth(BaseModel):
    username: str
    password: str = Field(..., max_length=72)
