FROM python:3.9
WORKDIR /main
COPY notes.py /main
COPY templates /main/templates
RUN pip install flask
CMD ["python", "notes.py"]
