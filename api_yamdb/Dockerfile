
FROM python:3.7-slim

WORKDIR /app

COPY api_yamdb/requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY ./ .

# ENV PIP_ROOT_USER_ACTION=ignore

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
