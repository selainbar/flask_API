 FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY C:\Users\USER\Desktop\program\RESTful API\Students_API.py

CMD ["python", "Students_API.py"]

