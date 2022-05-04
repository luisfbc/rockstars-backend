# Set Python image
FROM python:3.10.4-bullseye
# Prevents infinite buffering
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /usr/src/django/
RUN mkdir /usr/src/django/music_store
# Set the working directory to /musicapi
WORKDIR /usr/src/django/music_store
# Copy the current directory contents into the container at /music_store
ADD . /usr/src/django/music_store
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt