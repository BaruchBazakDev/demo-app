FROM python:alpine3.15
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
