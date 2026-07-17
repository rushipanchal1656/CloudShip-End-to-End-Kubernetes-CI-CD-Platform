# Dockerfile for the CloudShip application. This Dockerfile uses the official Python 3.10 slim image as the base image. It creates a non-root user named "appuser" and sets the working directory to "/app". The application code is copied from the "app" directory, and the required Python packages are installed from the "requirements.txt" file. The container runs as the "appuser" user, exposes port 5000, and starts the application by executing "python app.py".

FROM python:3.10-slim

RUN useradd -m appuser
WORKDIR /app

COPY app/ .
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
