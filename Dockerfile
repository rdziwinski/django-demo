# Import base image
FROM python:3.9-bullseye

RUN apt-get update; apt-get upgrade

RUN python3 -m pip install Django
