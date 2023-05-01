
FROM python:3.7-slim

WORKDIR /app/api_yamdb/

COPY requirements.txt .

RUN pip3 install --upgrade pip  --no-cache-dir


RUN pip install -r /app/equirements.txt --no-cache-dir

COPY . .

# ENV PIP_ROOT_USER_ACTION=ignore

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
