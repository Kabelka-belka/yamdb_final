![example workflow](https://github.com/CreedOfFear/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

#  Автор
Кабелка Анна

## Как запустить проект:
______
### Клонируем репозиторий и переходим в него:
git clone git@github.com:Kabelka-belka/
yamdb_final.git   
cd infra_sp2   
cd api_yamdb

### Создаем и активируем виртуальное окружение:

python3 -m venv venv   
source /venv/bin/activate    
python -m pip install --upgrade pip

### Ставим зависимости из requirements.txt:
pip install -r requirements.txt

### Переходим в папку с файлом docker-compose.yaml:
cd infra

### Поднимаем контейнеры (infra_db, infra_web, infra_nginx):
docker-compose up -d --build

### Выполняем миграции:
docker-compose exec web python manage.py makemigrations reviews

docker-compose exec web python manage.py migrate

### Создаем суперпользователя:
docker-compose exec web python manage.py createsuperuser

### Собираем статику:
docker-compose exec web python manage.py collectstatic --no-input

### Останавливаем контейнеры:
docker-compose down -v