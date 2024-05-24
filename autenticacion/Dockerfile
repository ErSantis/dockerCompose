FROM python:3.9
WORKDIR /main
COPY auth.py /main
COPY templates /main/templates
RUN pip install flask
CMD ["python", "auth.py"]