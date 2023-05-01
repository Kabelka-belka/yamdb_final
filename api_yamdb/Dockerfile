
FROM python:3.7-slim

WORKDIR /app/api_yamdb/

COPY ./ /app

RUN pip3 install -r /yamdb_final/api_yamdb/requirements.txt --no-cache-dir

# ENV PIP_ROOT_USER_ACTION=ignore

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
