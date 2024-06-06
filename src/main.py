from fastapi import FastAPI
from auth.base_config import auth_backend, fastapi_users, current_active_user, current_superuser
from auth.schemas import UserRead, UserCreate, UserUpdate
from skins.router import router as skin_router
from news.router import router as router_news

app = FastAPI(
    title="Trading App"
)


# Аутентификация и регистрация
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"]
)

app.include_router(skin_router, prefix="/skins", tags=["skins"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router_operation)

# Новости
app.include_router(router_news, prefix="/news", tags=["News"])

