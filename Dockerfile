FROM python:3.14
WORKDIR /app
RUN apt-get update && apt-get install && pip install colorama psutil  
COPY main.py . 
CMD ["python","main.py"]

