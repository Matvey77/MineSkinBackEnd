from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from database import get_async_session
from . import crud, models, schemas
from auth.base_config import current_active_user, current_superuser
from auth.models import User

router = APIRouter()

@router.post("/", response_model=schemas.Skin)
async def create_skin(skin: schemas.SkinCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(current_active_user)):
    return await crud.create_skin(db=db, skin=skin, author_id=current_user.id)

@router.get("/{skin_id}", response_model=schemas.Skin)
async def read_skin(skin_id: int, db: AsyncSession = Depends(get_async_session)):
    db_skin = await crud.get_skin(db, skin_id=skin_id)
    if db_skin is None:
        raise HTTPException(status_code=404, detail="Skin not found")
    return db_skin

@router.get("/", response_model=List[schemas.Skin])
async def read_skins(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    skins = await crud.get_skins(db, skip=skip, limit=limit)
    return skins

@router.put("/{skin_id}", response_model=schemas.Skin)
async def update_skin(skin_id: int, skin: schemas.SkinUpdate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(current_active_user)):
    db_skin = await crud.get_skin(db, skin_id=skin_id)
    if db_skin is None:
        raise HTTPException(status_code=404, detail="Skin not found")
    if db_skin.author_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return await crud.update_skin(db=db, db_skin=db_skin, skin_update=skin)

@router.delete("/{skin_id}", response_model=schemas.Skin)
async def delete_skin(skin_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(current_active_user)):
    db_skin = await crud.get_skin(db, skin_id=skin_id)
    if db_skin is None:
        raise HTTPException(status_code=404, detail="Skin not found")
    if db_skin.author_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return await crud.delete_skin(db=db, db_skin=db_skin)

# Маршруты для комментариев
@router.post("/{skin_id}/comments/", response_model=schemas.Comment)
async def create_comment(skin_id: int, comment: schemas.CommentCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(current_active_user)):
    return await crud.create_comment(db=db, comment=comment, skin_id=skin_id, author_id=current_user.id)

@router.get("/{skin_id}/comments/", response_model=List[schemas.Comment])
async def read_comments(skin_id: int, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    comments = await crud.get_comments_by_skin(db, skin_id=skin_id, skip=skip, limit=limit)
    return comments

@router.put("/comments/{comment_id}", response_model=schemas.Comment)
async def update_comment(comment_id: int, comment: schemas.CommentUpdate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(current_active_user)):
    db_comment = await crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comment.author_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return await crud.update_comment(db=db, db_comment=db_comment, comment_update=comment)

@router.delete("/comments/{comment_id}", response_model=schemas.Comment)
async def delete_comment(comment_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(current_active_user)):
    db_comment = await crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if db_comment.author_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return await crud.delete_comment(db=db, db_comment=db_comment)

# Маршруты для поиска скинов
@router.get("/search/by-tag/", response_model=List[schemas.Skin])
async def search_skins_by_tag(tag: int, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    skins = await crud.search_skins_by_tag(db, tag=tag, skip=skip, limit=limit)
    return skins

@router.get("/search/by-name/", response_model=List[schemas.Skin])
async def search_skins_by_name(name: str, skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    skins = await crud.search_skins_by_name(db, name=name, skip=skip, limit=limit)
    return skins
