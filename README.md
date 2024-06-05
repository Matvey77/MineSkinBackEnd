# MineSkinBackEnd

### СТРУКТУРА ПРОЕКТА

fastapi-project
├── migrations/
├── src
│   ├── "вопрос-ответ"
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   ├── "регистрация"
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   ├── "новости"
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   ├── "каталог-скинов"
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
├── .env
├── .gitignore
└── alembic.ini


# FastAPI Project

## Описание

Этот проект является примером реализации бэкенда с использованием FastAPI, структурированного в соответствии с принципами DDD (Domain-Driven Design) и Clean Architecture. Проект включает в себя рабочее API с документацией SwaggerUI и подключенной базой данных.

## Структура проекта

fastapi-project
├── migrations/
├── src.
│ ├── core.
│ │ ├── config.py # Настройки проекта.
│ │ ├── database.py # Подключение к БД.
│ │ ├── security.py # Безопасность (например, JWT).
│ ├── api.
│ │ ├── deps.py # Зависимости API.
│ │ ├── v1.
│ │ │ ├── api.py # Главный файл для регистрации маршрутов.
│ │ │ ├── question_answer.py # Маршруты question-answer.
│ │ │ ├── auth.py # Маршруты registration.
│ │ │ ├── registration.py # Маршруты registration.
│ │ │ ├── news.py # Маршруты news.
│ │ │ ├── skins_catalog.py # Маршруты skins-catalog.
│ ├── question_answer.
│ │ ├── models.py # Модели БД.
│ │ ├── schemas.py # Pydantic модели.
│ │ ├── repository.py # Логика работы с БД.
│ │ ├── services.py # Бизнес-логика.
│ ├── registration.
│ │ ├── models.py # Модели БД.
│ │ ├── schemas.py # Pydantic модели.
│ │ ├── repository.py # Логика работы с БД.
│ │ ├── services.py # Бизнес-логика.
│ ├── news.
│ │ ├── models.py # Модели БД.
│ │ ├── schemas.py # Pydantic модели.
│ │ ├── repository.py # Логика работы с БД.
│ │ ├── services.py # Бизнес-логика.
│ ├── skins_catalog.
│ │ ├── models.py # Модели БД.
│ │ ├── schemas.py # Pydantic модели.
│ │ ├── repository.py # Логика работы с БД.
│ │ ├── services.py # Бизнес-логика.
│ ├── main.py # Точка входа.
├── .env.
├── .gitignore.
└── alembic.ini.


### Описание директорий

- **migrations/**: Каталог для хранения файлов миграций базы данных.
- **src/**: Корневая директория исходного кода проекта.
  - **core/**: Содержит конфигурации, подключение к базе данных и логику безопасности.
    - `config.py`: Настройки проекта.
    - `database.py`: Подключение к базе данных.
    - `security.py`: Логика безопасности (например, JWT).
  - **api/**: Содержит зависимости для API и маршруты (в данном случае, версия 1).
    - `deps.py`: Зависимости API.
    - **v1/**: Версия 1 API.
      - `api.py`: Главный файл для регистрации маршрутов.
      - `question_answer.py`: Маршруты для модуля question-answer.
      - `registration.py`: Маршруты для модуля registration.
      - `news.py`: Маршруты для модуля news.
      - `skins_catalog.py`: Маршруты для модуля skins-catalog.
  - **question_answer/**: Директория модуля question-answer.
    - `models.py`: Модели базы данных.
    - `schemas.py`: Pydantic модели.
    - `repository.py`: Логика работы с базой данных.
    - `services.py`: Бизнес-логика.
  - **registration/**: Директория модуля registration.
    - `models.py`: Модели базы данных.
    - `schemas.py`: Pydantic модели.
    - `repository.py`: Логика работы с базой данных.
    - `services.py`: Бизнес-логика.
  - **news/**: Директория модуля news.
    - `models.py`: Модели базы данных.
    - `schemas.py`: Pydantic модели.
    - `repository.py`: Логика работы с базой данных.
    - `services.py`: Бизнес-логика.
  - **skins_catalog/**: Директория модуля skins-catalog.
    - `models.py`: Модели базы данных.
    - `schemas.py`: Pydantic модели.
    - `repository.py`: Логика работы с базой данных.
    - `services.py`: Бизнес-логика.
  - `main.py`: Точка входа приложения.

## Запуск проекта



