![Test and push to Docker Hub](https://github.com/doroshenkokb/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Проект Database_of_reviews

## Описание

Проект 
Database_of_reviews собирает отзывы пользователей на произведения.Произведения делятся на категории: "Категории", "Фильмы", "Музыка".Список категорий (Category) может быть расширен администратором.

#### Доступный функционал

- Для аутентификации используются JWT-токены.
- У неаутентифицированных пользователей доступ к API только на уровне чтения.
- Создание объектов разрешено только аутентифицированным пользователям.На прочий фунционал наложено ограничение в виде административных ролей и авторства.
- Управление пользователями.
- Получение списка всех категорий и жанров, добавление и удаление.
- Получение списка всех произведений, их добавление.Получение, обновление и удаление конкретного произведения.
- Получение списка всех отзывов, их добавление.Получение, обновление и удаление конкретного отзыва.  
- Получение списка всех комментариев, их добавление.Получение, обновление и удаление конкретного комментария.
- Возможность получения подробной информации о себе и удаления своего аккаунта.
- Фильтрация по полям.

#### Технологии

- Python 3.7
- Django 3.2
- Django Rest Framework 3.12.4
- Simple JWT
- SQLite3

## Установка

1. Клонировать репозиторий:

    ```python
    git clone https://github.com/doroshenkokb/Database_of_reviews.git
    ```

2. Создать `.env` файл на уровне с файлом `docker-compose.yaml` в директории infra с указаниме данных:

    - SECRET_KEY - секретный ключ Django;
    - DB_ENGINE - движок базы данных (БД) postgresql: `django.db.backends.postgresql`;
    - DB_NAME - имя БД: `postgres`;
    - POSTGRES_USER - пользователь БД: `postgres`;
    - POSTGRES_PASSWORD - пароль рользователя БД: `postgres`;
    - DB_HOST - адрес удалённого сервера БД, по умолчанию: `db`;
    - DB_PORT - порт сервера базы данных: `5432`;

3. Создать и активировать виртуальное пространство, установить зависимости и запустить тесты:

    Для Windows:

    ```python
    cd yamdb_final
    python -m venv venv
    source venv/Scripts/activate
    cd api_yamdb
    pip install -r requirements.txt
    cd ..
    pytest
    ```

    Для Mac/Linux:

    ```python
    cd yamdb_final
    python3 -m venv venv
    source venv/bin/activate
    cd api_yamdb
    pip install -r requirements.txt
    cd ..
    pytest
    ```

4. Запустить контейнер Docker:

    - Проверить статус Docker:

    ```python
    docker --version
    ```

    - Запустить docker-compose:

    ```python
    cd infra/
    docker-compose up -d
    ```

5. Выполнить миграции, создать суперпользователя и мигрировать статику:

    ```python
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    docker-compose exec web python manage.py collectstatic --no-input
    ```

6. Для запуска в виртуальном окружении, после создания и активации виртуального пространства, установки зависимостей, запустить проект локально:

    Для Windows:

    ```python
    python manage.py runserver
    ```

    Для Mac/Linux:

    ```python
    python3 manage.py runserver
    ```

7. Проверить доступность сервиса:

    ```python
    http://localhost/admin
    ```

#### Автор

Дорошенко Кирилл - [https://github.com/doroshenkokb](https://github.com/doroshenkokb)
