# Dockerfile for auth_service
FROM python:3.9
WORKDIR /app
COPY auth_server.py /app
RUN pip install flask
CMD ["python", "auth_server.py"]