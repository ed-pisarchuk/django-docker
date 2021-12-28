# Django-проект "Архив книг и журналов"

## Руководство по запуску проекта:

1. Собрать и запустить контейнер с приложение одним из ниже описанных способов:  
   a. Загрузить проект локально и в корне проекта выполнить команду docker-compose up
   b. Загрузить проект локально и в корне проекта выполнить команды:
   ```shell
   docker build -t django-docker_app:v2 .
   docker run -it --name django-docker_app -p 8000:8000 django-docker_app:v2
   ```


2. Перейти по пути http://127.0.0.1:8000/admin/ и проверить добавление и редактирование сущностей: издательства, книги, журналы, статьи


3. Проверить на работоспособность слеующие эндпоинты:
    - /pools/publishers/ (GET/POST)
    - /pools/publishers/{id} (GET/PUT/PATCH/DELETE)
    - /pools/journals/ (GET/POST)
    - /pools/journals/{id} (GET/PUT/PATCH/DELETE)
    - /pools/books/ (GET/POST)
    - /pools/books/{id} (GET/PUT/PATCH/DELETE)
    - /pools/journals/ (GET/POST)
    - /pools/journals/{id} (GET/PUT/PATCH/DELETE)
    - /store/journals/{id}/articles/ GET

4. Запустить выполнение интеграционных тестов командой pytest


5. Очистить созданные образ и контейнер:
    
   a. При сборке и запуске используя `docker-compose`:
   ```shell
   docker rm django-docker_app_1
   docker rmi django-docker_app:latest
   ```
   b. При сборке и запуске используя `docker`:
   ```shell
   docker rm django-docker_app
   docker rmi django-docker_app:v2
   ```
