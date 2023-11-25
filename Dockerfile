FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY client ./client
COPY application.yml .

RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]