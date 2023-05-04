![example workflow](https://github.com/CreedOfFear/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

#  Автор
Кабелка Анна

## Проект доступен по адресу: 

http://localhost:8080

## Шаблон .env:

+  указываем, с какой БД работаем
DB_ENGINE=django.db.backends.postgresql
+  имя базы данных
DB_NAME=
+ логин для подключения к базе данных
POSTGRES_USER=
+  пароль для подключения к БД (установите свой)
POSTGRES_PASSWORD=
+ название сервиса (контейнера)
DB_HOST=
+ порт для подключения к БД
DB_PORT=
SECRET_KEY=<секретный ключ проекта django> 

## Как запустить проект:
______

Для запуска проекта в контейнерах используем docker-compose : docker-compose up -d --build, находясь в директории с docker-compose.yaml

## После сборки :

+ Выполняем миграции
docker-compose exec web python manage.py migrate
+ Создаем суперппользователя
docker-compose exec web python manage.py createsuperuser
+ Собираем статику со всего проекта
docker-compose exec web python manage.py collectstatic --no-input
+ Для дампа данных из БД
docker-compose exec web python manage.py dumpdata > dump.json

___

Пройдите по адресу http://localhost:8080/admin/ , авторизуйтесь как созданный выше суперпользователь, и внесите записи в базу данных через админ панель.
___


### Останавливить контейнеры:
docker-compose down -v