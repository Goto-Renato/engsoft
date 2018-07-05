FROM python:2
ENV PYTHONUNBUFFERED 1	

RUN mkdir /webapp
WORKDIR /webapp

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
ADD requirements.txt /webapp/
RUN pip install -r /webapp/requirements.txt

ADD . /webapp/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

