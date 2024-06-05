from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from . import schemas, models

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)

@router.post("/", response_model=schemas.Question)
async def create_question(question: schemas.QuestionCreate, db: AsyncSession = Depends(get_async_session)):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    await db.commit()
    await db.refresh(db_question)
    return db_question

@router.delete("/{question_id}")
async def delete_question(question_id: int, db: AsyncSession = Depends(get_async_session)):
    question = await db.get(models.Question, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    await db.delete(question)
    await db.commit()
    return {"message": "Question deleted successfully"}

@router.put("/{question_id}", response_model=schemas.Question)
async def update_question(question_id: int, question: schemas.QuestionCreate, db: AsyncSession = Depends(get_async_session)):
    db_question = await db.get(models.Question, question_id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    for key, value in question.dict().items():
        setattr(db_question, key, value)
    await db.commit()
    await db.refresh(db_question)
    return db_question