FROM python:3.9
WORKDIR /worker1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "worker1.py"]

