FROM python:latest

WORKDIR /myapp

COPY app.py .

CMD ["python3", "app.py"]
