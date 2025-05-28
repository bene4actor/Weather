🌤️ Weather Forecast App

Простое Django-приложение, в котором можно ввести название города и получить прогноз погоды на ближайшее время с помощью [Open-Meteo API](https://open-meteo.com/).


🚀 Быстрый старт

Клонируешь репозиторий
git clone https://github.com/yourusername/weather-app.git
cd weather-app

Создаёшь файл с переменными окружения, например, .env
cp .env.example .env


⚙️ Настройка `.env`

Заполни `.env` примерно так (замени значения на свои):

DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=weather_db
DB_USER=weather_user
DB_PASSWORD=strong_password
DB_HOST=db
DB_PORT=5432


🐳 Запуск в Docker

# Собираем и запускаем контейнеры в фоне
docker compose up -d --build

# Применяем миграции базы данных
docker compose exec web python manage.py migrate

# (Опционально) Создаём администратора для Django Admin
docker compose exec web python manage.py createsuperuser


🌐 Доступ к приложению

* Сайт: [http://localhost:8000/](http://localhost:8000/)
* Админка Django: [http://localhost:8000/admin/](http://localhost:8000/admin/)


🧪 Запуск тестов

# Внутри контейнера
docker compose exec web pytest

# Или локально (если настроена БД с хостом localhost)
pytest


📦 Технологии

* Python 3.12 + Django
* PostgreSQL
* Docker + Docker Compose
* Gunicorn — WSGI сервер для продакшна
* Open-Meteo API — получение погоды
* Pytest — юнит-тесты


✅ Функционал

* Ввод города и отображение прогноза погоды
* Сохранение истории запросов
* API для статистики запросов по городам
* Повторное посещение — показывается последний просмотренный город
* Готово для запуска в Docker с продакшн-сервером Gunicorn


Советы по развитию проекта

* Можно добавить кэширование запросов к Open-Meteo API для ускорения
* Добавить frontend с React или Vue для интерактивности
* Настроить CI/CD для автоматического деплоя
