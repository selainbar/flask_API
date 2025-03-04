 FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY Students_API.py .

EXPOSE 5001

CMD ["python", "Students_API.py"]

