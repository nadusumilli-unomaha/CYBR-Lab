###################################
#
# CYBR8470 Dev Docker Container
# @author Nikhit Adusumilli
#
###################################

# Pull base image.
FROM python:2.7.13
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image

WORKDIR /var/www/backend

ADD requirements.txt /var/www/backend/

#Python packages
RUN pip install -r requirements.txt

ADD . /var/www/backend/
