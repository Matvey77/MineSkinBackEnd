from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_db
from src.news import models, schemas
from src.auth import get_current_active_user, get_current_active_admin

router = APIRouter()

# Получение всех новостей
@router.get("/news/", response_model=list[schemas.News])
async def read_news(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.News).offset(skip).limit(limit))
    news_items = result.scalars().all()
    return news_items

# Создание новости
@router.post("/news/", response_model=schemas.News)
async def create_news(news: schemas.NewsCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_active_admin)):
    db_news = models.News(**news.dict())
    db.add(db_news)
    await db.commit()
    await db.refresh(db_news)
    return db_news

# Получение конкретной новости
@router.get("/news/{news_id}", response_model=schemas.News)
async def read_news_item(news_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.News).filter(models.News.id == news_id))
    db_news = result.scalar_one_or_none()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news

# Обновление новости
@router.put("/news/{news_id}", response_model=schemas.News)
async def update_news(news_id: int, news: schemas.NewsUpdate, db: AsyncSession = Depends(get_db), user = Depends(get_current_active_admin)):
    result = await db.execute(select(models.News).filter(models.News.id == news_id))
    db_news = result.scalar_one_or_none()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    for key, value in news.dict().items():
        setattr(db_news, key, value)
    await db.commit()
    await db.refresh(db_news)
    return db_news

# Удаление новости
@router.delete("/news/{news_id}", response_model=schemas.News)
async def delete_news(news_id: int, db: AsyncSession = Depends(get_db), user = Depends(get_current_active_admin)):
    result = await db.execute(select(models.News).filter(models.News.id == news_id))
    db_news = result.scalar_one_or_none()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    await db.delete(db_news)
    await db.commit()
    return db_news
