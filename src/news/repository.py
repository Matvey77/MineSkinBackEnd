from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.news.models import News
from src.news.schemas import NewsCreate, NewsUpdate

async def get_news(db: AsyncSession, news_id: int):
    result = await db.execute(select(News).filter(News.id == news_id))
    return result.scalars().first()

async def get_news_list(db: AsyncSession):
    result = await db.execute(select(News))
    return result.scalars().all()

async def create_news(db: AsyncSession, news: NewsCreate):
    db_news = News(**news.dict())
    db.add(db_news)
    await db.commit()
    await db.refresh(db_news)
    return db_news

async def update_news(db: AsyncSession, news_id: int, news: NewsUpdate):
    db_news = await get_news(db, news_id)
    if db_news:
        for key, value in news.dict().items():
            setattr(db_news, key, value)
        await db.commit()
        await db.refresh(db_news)
        return db_news
    return None

async def delete_news(db: AsyncSession, news_id: int):
    db_news = await get_news(db, news_id)
    if db_news:
        await db.delete(db_news)
        await db.commit()
        return db_news
    return None
