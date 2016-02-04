#Dockerfile to create django-annotation image
FROM datashed/centos_py3
RUN mkdir /code
WORKDIR /code
COPY ./requirements/base.txt /code/
RUN pip3 install -r base.txt
