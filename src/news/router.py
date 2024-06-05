from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from src.database import get_db
from src.news import models, schemas
from src.auth import get_current_active_user, get_current_active_admin

router = APIRouter()

# Получение всех новостей
@router.get("/news/", response_model=list[schemas.News])
async def read_news(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.News).offset(skip).limit(limit).options(joinedload(models.News.tags)))
    news_items = result.scalars().all()
    return news_items

# Поиск новостей по тэгу
@router.get("/news/search/", response_model=list[schemas.News])
async def search_news_by_tag(tag: str, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.News).join(models.News.tags).filter(models.Tag.name == tag).offset(skip).limit(limit).options(joinedload(models.News.tags)))
    news_items = result.scalars().all()
    return news_items

# Создание новости
@router.post("/news/", response_model=schemas.News)
async def create_news(news: schemas.NewsCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_active_admin)):
    db_news = models.News(title=news.title, content=news.content)
    for tag in news.tags:
        db_tag = await db.execute(select(models.Tag).filter(models.Tag.name == tag.name))
        db_tag = db_tag.scalar_one_or_none()
        if not db_tag:
            db_tag = models.Tag(name=tag.name)
        db_news.tags.append(db_tag)
    db.add(db_news)
    await db.commit()
    await db.refresh(db_news)
    return db_news

# Получение конкретной новости
@router.get("/news/{news_id}", response_model=schemas.News)
async def read_news_item(news_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.News).filter(models.News.id == news_id).options(joinedload(models.News.tags)))
    db_news = result.scalar_one_or_none()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news

# Обновление новости
@router.put("/news/{news_id}", response_model=schemas.News)
async def update_news(news_id: int, news: schemas.NewsUpdate, db: AsyncSession = Depends(get_db), user = Depends(get_current_active_admin)):
    result = await db.execute(select(models.News).filter(models.News.id == news_id).options(joinedload(models.News.tags)))
    db_news = result.scalar_one_or_none()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    db_news.title = news.title
    db_news.content = news.content
    db_news.tags.clear()
    for tag in news.tags:
        db_tag = await db.execute(select(models.Tag).filter(models.Tag.name == tag.name))
        db_tag = db_tag.scalar_one_or_none()
        if not db_tag:
            db_tag = models.Tag(name=tag.name)
        db_news.tags.append(db_tag)
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
