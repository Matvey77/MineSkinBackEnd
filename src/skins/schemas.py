from pydantic import BaseModel
from typing import Optional

class SkinBase(BaseModel):
    name: str
    description: Optional[str] = None
    tag: int
    skin_src: Optional[str] = None

class SkinCreate(SkinBase):
    pass

class SkinUpdate(SkinBase):
    pass

class SkinInDBBase(SkinBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

class Skin(SkinInDBBase):
    pass

class SkinInDB(SkinInDBBase):
    pass

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class CommentUpdate(CommentBase):
    pass

class CommentInDBBase(CommentBase):
    id: int
    skin_id: int
    author_id: int

    class Config:
        orm_mode = True

class Comment(CommentInDBBase):
    pass

class CommentInDB(CommentInDBBase):
    pass
