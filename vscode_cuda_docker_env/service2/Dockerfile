FROM tensorflow/tensorflow:latest-gpu AS base

WORKDIR /workspace
COPY ./requirements.txt /workspace/requirements.txt
RUN pip install -r requirements.txt
