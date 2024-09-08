FROM python:3.10.14-slim

RUN apt-get update && apt-get install -y wait-for-it

WORKDIR /usr/scr/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/scr/app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]