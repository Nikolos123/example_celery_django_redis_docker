from celery import shared_task
from django.core.mail import send_mail

from main.models import Contact
from main.service import send
from  src.celery import app

@app.task#Обязательно обвернуть функцию
def send_spam_email(user_email):#не передаем рез
    send(user_email)
    # for i in range(10):
    #     send_mail(
    #         'Вы подписались на рассылку',
    #         'Мы будем присылать Вам много спама.',
    #         'django.celery.redis@gmail.com',
    #         [user_email],
    #         fail_silently=False
    #     )

@app.task#Обязательно обвернуть функцию
def send_beat_email():#не передаем рез
   #попросить email
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать Вам много спама каждую минуту.',
            'django.celery.redis@gmail.com',
            [contact.email],
            fail_silently=False
        )



@app.task
def my_task(a,b):
    c=a+b
    return c

@app.task
def my_task_as(a,e):
    c=a+e
    return c


@app.task(bind=True,default_retry_delay=5*60)
def my_task_retry(self,x,y):
    try:
        return x+y
    except Exception as exc:
        raise self.retry(exc=exc,countdown=60)
@shared_task()#если пишем свои библиотеки используем(если не для определенного проекта)
def my_sh_task(msg):
    return msg+"!!!"
