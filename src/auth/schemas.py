from pydantic import BaseModel
from typing import Optional

class UserRead(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
