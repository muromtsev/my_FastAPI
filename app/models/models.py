from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class FeedBack(BaseModel):
    name: str
    message: str

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool

class LoginUser(BaseModel):
    username: str
    password: str