from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def get_skin(db: AsyncSession, skin_id: int):
    result = await db.execute(select(models.Skin).filter(models.Skin.id == skin_id))
    return result.scalars().first()

async def get_skins(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Skin).offset(skip).limit(limit))
    return result.scalars().all()

async def create_skin(db: AsyncSession, skin: schemas.SkinCreate, author_id: int):
    db_skin = models.Skin(**skin.dict(), author_id=author_id)
    db.add(db_skin)
    await db.commit()
    await db.refresh(db_skin)
    return db_skin

async def update_skin(db: AsyncSession, db_skin: models.Skin, skin_update: schemas.SkinUpdate):
    for var, value in vars(skin_update).items():
        setattr(db_skin, var, value) if value else None
    await db.commit()
    await db.refresh(db_skin)
    return db_skin

async def delete_skin(db: AsyncSession, db_skin: models.Skin):
    await db.delete(db_skin)
    await db.commit()
    return db_skin

# CRUD функции для комментариев
async def get_comment(db: AsyncSession, comment_id: int):
    result = await db.execute(select(models.Comment).filter(models.Comment.id == comment_id))
    return result.scalars().first()

async def get_comments_by_skin(db: AsyncSession, skin_id: int, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Comment).filter(models.Comment.skin_id == skin_id).offset(skip).limit(limit))
    return result.scalars().all()

async def create_comment(db: AsyncSession, comment: schemas.CommentCreate, skin_id: int, author_id: int):
    db_comment = models.Comment(**comment.dict(), skin_id=skin_id, author_id=author_id)
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment

async def update_comment(db: AsyncSession, db_comment: models.Comment, comment_update: schemas.CommentUpdate):
    for var, value in vars(comment_update).items():
        setattr(db_comment, var, value) if value else None
    await db.commit()
    await db.refresh(db_comment)
    return db_comment

async def delete_comment(db: AsyncSession, db_comment: models.Comment):
    await db.delete(db_comment)
    await db.commit()
    return db_comment

# Функции для поиска скинов по тегам и именам
async def search_skins_by_tag(db: AsyncSession, tag: int, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Skin).filter(models.Skin.tag == tag).offset(skip).limit(limit))
    return result.scalars().all()

async def search_skins_by_name(db: AsyncSession, name: str, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Skin).filter(models.Skin.name.ilike(f"%{name}%")).offset(skip).limit(limit))
    return result.scalars().all()
