#!/bin/bash

#/bin/python3.4 /code/manage.py migrate --settings=annotator.settings.production
#echo "Done migration."
/bin/python3.4 /code/manage.py runserver 0.0.0.0:8000 --settings=annotator.settings.production
echo "django app running."
tail -f /var/log/yum.log
