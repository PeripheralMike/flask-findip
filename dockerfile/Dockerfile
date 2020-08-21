FROM python:3.8.1

WORKDIR /

COPY app.py /

RUN pip install flask

RUN pip install ipgetter2

EXPOSE 8080

EXPOSE 5000

CMD [ "python" , "app.py" ]
