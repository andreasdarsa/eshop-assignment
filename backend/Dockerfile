FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install flask flask-cors pymongo
CMD ["python", "app.py"]