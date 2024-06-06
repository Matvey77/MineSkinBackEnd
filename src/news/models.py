from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

news_tags = Table('news_tags', Base.metadata,
    Column('news_id', Integer, ForeignKey('news.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class News(Base):
    __tablename__ = 'news'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    tags = relationship('Tag', secondary=news_tags, back_populates='news')

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    news = relationship('News', secondary=news_tags, back_populates='tags')
