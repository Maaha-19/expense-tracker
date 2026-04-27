from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: str

class ExpenseOut(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: str
    owner_id: int

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str