![Python](https://img.shields.io/badge/Python-3.12-_)
![Aiogram3](https://img.shields.io/badge/Aiogram-3-blue)
![Redis](https://img.shields.io/badge/Redis-6.2--alpine-red)
![Pydantic](https://img.shields.io/badge/Pydantic-2.5.3-yellow)
![Docker](https://img.shields.io/badge/Docker-24.0.6-blue)


# Telegram NLP Search Bot


## Настройка окружения
1. Создаем окружение:
   * macOS / Linux: ```python3 -m venv venv```
   * Windows: ```python -m venv venv```
2. Активируем окружение: 
   * macOS / Linux: ```source ./venv/bin/activate```
   * Windows: ```./venv/Scripts/Activate```
3. Устанавливаем пакеты: ```pip install -r requirements.txt```
4. Поднимаем docker контейнеры: 
   * macOS / Linux: ```sudo docker compose -f ./deployment/docker-compose.local.yaml up -d --build```
   * Windows: ```docker compose -f ./deployment/docker-compose.local.yaml up -d --build```


## Первый запуск
С помощью bash скрипта: ```sudo bash ./deployment/scripts/start.sh```

Ручной запуск:
1. Применяем миграции alembic: ```alembic upgrade head```
2. Проверяем подключение к БД:
   * macOS / Linux: ```python3 ./scripts/connection.py```
   * Windows: ```python ./scripts/connection.py```
3. Запускаем проект:
   * macOS / Linux: ```python3 ./cmd/bot/main.py```
   * Windows: ```python ./cmd/bot/main.py```


## Разработка

### Cтруктура проекта
    * /common - Вспомогательные зависимости
    * /config - Директория с настройками
        - /db - Настройки баз даннных
        - /settings
            - /settings.py - Основные настройки
    * /deps - Зависимости
    * /filters - Фильтры
    * /keyboards - Клавиатуры
    * /loader - Загрузка сущность бота
    * /nlp - Логика NLP модуля
    * /models - ORM модели для SQLAlchemy
    * /routers - Обработчики событий
    * /schemas - Pydantic модели
    * /server - Сервер бота
    * /services - Бизнес-логика
    * /usecases - Логика обработчиков событий

### Стиль кода
Перед каждым пушем прописываем следующие команды:
   * ```black .```
   * ```isort .```
   * ```ruff .```

А также можно включить pre-commit: ```install pre-commit``` 

### Git
1. Ведем 2 ветки: master и dev
2. Мержимся и пулимся к dev
3. Периодически сливаем изменения в master и обновляем версию проекта
4. На прод лить только протестированный master
5. Нейминг веток:
   * feature/<feature_name> - если написал что-то новое
   * fix/<fix_name> - если исправил какой-то баг
   * refactor/<refactor_name> - если переписал старый код


## Changelog
* Историю изменений по версиям фиксируем в ```changelog.md```
