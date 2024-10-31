FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN adduser --disabled-password celeryuser
USER celeryuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]