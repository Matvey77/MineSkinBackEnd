from pydantic import BaseModel
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    content: str

class NewsCreate(NewsBase):
    pass

class NewsUpdate(NewsBase):
    pass

class News(NewsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
