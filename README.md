![example workflow](https://github.com/PashkaVRN/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# YaMDb API

### Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения, позволяет ставить произведениям оценку и комментировать чужие отзывы.

Произведения делятся на категории, и на жанры. Список произведений, категорий и жанров может быть расширен администратором.

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Доступ к БД проекта осуществляется через Api.

Полный список запросов и эндпоинтов описан в документации ReDoc, доступна после запуска проекта по адресу:
```
http://158.160.39.8/redoc/
```
### Как запустить проект на тестовом сервере:
Клонировать репозиторий, перейти в директорию с проектом.

```
git clone git@github.com:PashkaVRN/yamdb_final.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/source/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Переходим в директорию с файлом docker-compose.yaml:
```bash
cd infra
```

### Запускаем Docker:
```bash
sudo systemctl start docker
```

### В директории infra создадим файл с переменными окружения:
```bash
touch .env
```
```bash
nano .env
```
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=test_base
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test_pass
DB_HOST=127.0.0.1
DB_PORT=5432
```