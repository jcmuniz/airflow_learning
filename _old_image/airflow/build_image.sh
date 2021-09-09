#!/bin/bash
AIRFLOW_VERSION=2.1.3
IMAGE_VERSION=${AIRFLOW_VERSION} 
#-python3.9
#docker login --username julianomuniz
docker build --no-cache -t julianomuniz/airflow:${IMAGE_VERSION} .
#docker tag airflow-python:${AIRFLOW_VERSION} julianomuniz/airflow-python:${AIRFLOW_VERSION}
#docker tag airflow-python:latest julianomuniz/airflow-python:latest
docker push julianomuniz/airflow:${IMAGE_VERSION}
#docker push julianomuniz/airflow-python:latest