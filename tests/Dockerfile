FROM python:alpine3.15

WORKDIR /tests

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]


