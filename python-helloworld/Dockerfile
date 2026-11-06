FROM python:3.12-slim
LABEL maintainer="arthur"

COPY . /app 
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python","app.py"]
