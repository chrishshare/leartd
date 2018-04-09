FROM python:3.6.4
ENV PYTHONUMBUFFERED 1
RUN mkdir /leartd
RUN mkdir /leartd/dockermysql
WORKDIR /leartd
ADD requirements.txt /leartd/
RUN pip install -r requirements.txt
ADD . /leartd/
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN PYT