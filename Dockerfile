FROM selenium/standalone-firefox:latest

USER root

RUN apt-get update && \
    apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

USER seluser
