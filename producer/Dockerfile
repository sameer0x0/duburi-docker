FROM python:3.9
WORKDIR /producer
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "producer.py"]

