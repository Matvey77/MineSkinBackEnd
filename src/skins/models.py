from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Skin(Base):
    __tablename__ = "skin"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    tag = Column(Integer, index=True)
    skin_src = Column(Text)
    author_id = Column(Integer, ForeignKey("user.id"))
    comments = relationship("Comment", back_populates="skin")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    skin_id = Column(Integer, ForeignKey("skin.id"))
    author_id = Column(Integer, ForeignKey("user.id"))
    skin = relationship("Skin", back_populates="comments")
    author = relationship("User")
