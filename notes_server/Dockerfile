# Dockerfile for notes_service
FROM python:3.9
WORKDIR /app
COPY notes_server.py /app
RUN pip install flask
CMD ["python", "notes_server.py"]
