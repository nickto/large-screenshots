# Minimal image for deployment
FROM selenium/standalone-firefox:latest as deployment

USER root

RUN apt-get update && \
    apt-get install -y python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

USER seluser

# Larger image for development
FROM deployment as development

USER root

RUN apt-get install -y \
    git \
    zsh \
    vim

RUN pip3 install \
    yapf \
    rope \
    pylint    

USER seluser