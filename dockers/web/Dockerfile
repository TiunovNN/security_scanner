FROM python:3.6-stretch

RUN apt-get install -y libssl-dev libffi-dev gcc
RUN apt-get install -y libpq-dev libcairo2 libcairo2 \
                        libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0\
                         libffi-dev shared-mime-info

RUN adduser microblog

WORKDIR /home/microblog

RUN pip install gunicorn
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src app
RUN chown -R microblog:microblog ./
USER microblog
ENV FLASK_APP main.py
WORKDIR /home/microblog/app


EXPOSE 5000