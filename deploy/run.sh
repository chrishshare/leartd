#!/bin/sh
source ../django/bin/activate
#cd leartd
pip install -r requirements.txt
python manage.py collectstatic
python3 manage.py runserver 0.0.0.0:9000 --insecure &
