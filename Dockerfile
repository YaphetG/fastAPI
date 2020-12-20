FROM python:3.8.6

RUN apt-get update
RUN apt-get install -y git

RUN mkdir -p /home/code

WORKDIR /home/code

RUN git clone https://github.com/YaphetG/fastAPI.git

ENV PYTHONPATH=/home/code/fastAPI

WORKDIR /home/code/fastAPI

USER 1000

ENTRYPOINT ['python', 'src/api.py']

