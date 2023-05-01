
FROM python:3.7-slim

WORKDIR /app/api_yamdb/

COPY ./ /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

ENV PIP_ROOT_USER_ACTION=ignore

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
