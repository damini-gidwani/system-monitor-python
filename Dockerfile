FROM python:3.14-slim

WORKDIR /app

COPY main.py .

RUN pip install --no-cache-dir colorama psutil

CMD ["python", "main.py"]
