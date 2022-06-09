FROM python:3.9
# LABEL maintainer="LETEMBE ORPHEE"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


