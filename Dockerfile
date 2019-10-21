FROM python:3-alpine

ENV APP_HOME=/app DEVELOPER="Fernando Gonzalez"
WORKDIR ${APP_HOME}

ADD . /app

RUN pip install -r requirements.txt


CMD [ "./app.py" ]
ENTRYPOINT [ "python" ]

#Docker 

#1. docker build -t fernando7/movie:v1.0 .
#2. docker run -it --rm fernando`7/movie:v1.0
#docker run -it --rm -d -p 5000:5000 fernando7/movie:v1.7 

#http://192.168.99.100:5000/ this is the url where i can see the app running.
