FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get upgrade -y

RUN python3 -m pip install --upgrade pip

RUN apt-get install nano -y

RUN apt-get install gettext -y

COPY . .

EXPOSE 8000

RUN adduser --disabled-password celeryuser

RUN touch /app/debug.log && chmod 666 /app/debug.log

RUN chown celeryuser:celeryuser /app/debug.log

USER celeryuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]