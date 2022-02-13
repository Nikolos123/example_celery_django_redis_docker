install library
*****************
pip install celery
pip install redis
https://docs.celeryproject.org/en/master/getting-started/first-steps-with-celery.html#first-steps

подымаем докер с redis(устанавливаем докер)
docker run -d -p 6379:6379 redis


add __init__
************************************
from celery import app as celery_app

__all__ = ('celery_app',)


# from  __future__ import absolute_import,unicode_literals
# from celery import app as celery_app



для запуска нужно сделать файл task и стартануть все worker

celery -A send_email("имя из настроик celery") worker -l info(хотим видить логи)
celery -A send_email worker -l info


полезные ссылки
https://docs.celeryproject.org/en/latest/internals/reference/celery.utils.collections.html#celery.utils.collections.ChainMap.setdefault
https://docs.celeryproject.org/en/master/getting-started/first-steps-with-celery.html

переодичность
https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html

restart all service after start
celery -A send_email worker -l info



******************************************
part 2
add task new

flower celery django
https://flower.readthedocs.io/en/latest/install.html#usage-examples
https://flower.readthedocs.io/en/latest/docker.html(docker)
pip install flower
flower -A send_email --port=5555

celery --broker redis://0.0.0.0:6379/0  flower -A send_email --port=5555

python console 
my_task.delay(1,2)

try:task

запуск в отоленном режите
my_task.apply_async((1,2),countdown = 60)


добавляем к результату функции
my_task.apply_async((1,2),link=my_task.s(20))