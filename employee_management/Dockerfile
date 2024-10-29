# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose the port
EXPOSE 8000

RUN adduser --disabled-password celeryuser
USER celeryuser

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]