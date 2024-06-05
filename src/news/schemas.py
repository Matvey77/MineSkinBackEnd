from pydantic import BaseModel
from datetime import datetime
from typing import List

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True

class NewsBase(BaseModel):
    title: str
    content: str

class NewsCreate(NewsBase):
    tags: List[TagCreate] = []

class NewsUpdate(NewsBase):
    tags: List[TagCreate] = []

class News(NewsBase):
    id: int
    created_at: datetime
    tags: List[Tag] = []

    class Config:
        orm_mode = True
