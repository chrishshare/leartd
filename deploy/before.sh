#!/bin/sh
deactivate
if [$? -eq 0]; then
   echo "virtualenv(django)环境退出成功！"
else
  echo "virtualenv(django)环境没有启动！"
rm -rfv /websites/leartd/staticweb/

source /websites/django/bin/activate
if [$? -eq 0]; then
  echo "virtualenv(django)环境启动成功！"
  python manage.py collectstatic
   python manage.py runserver 0.0.0.0:9000 --insecure &
else
   echo "virtualenv(django)环境启动失败！"
