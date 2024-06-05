from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from operations.router import router as router_operation
from news.router import router as router_news

app = FastAPI(
    title="Trading App"
)

# Аутентификация и регистрация
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

# Операции (существующие)
app.include_router(router_operation)

# Новости
app.include_router(router_news, prefix="/news", tags=["News"])
