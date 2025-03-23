FROM python:3.9
WORKDIR /worker2
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "worker2.py"]

