FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]