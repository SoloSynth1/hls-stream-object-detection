FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]