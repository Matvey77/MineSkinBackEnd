from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))  # Используем ForeignKey для связи с таблицей пользователей
    question = Column(String, nullable=False)