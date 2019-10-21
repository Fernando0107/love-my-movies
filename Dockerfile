FROM python:3-alpine

ENV APP_HOME=/app DEVELOPER="Fernando Gonzalez"
WORKDIR ${APP_HOME}

ADD . /app

RUN pip install -r requirements.txt

CMD [ "./app.py" ]
ENTRYPOINT [ "python" ]

#Docker 

#1. docker build -t fernando7/movie:v1.0 .
#2. docker run -it --rm fernando7/movie:v1.0
