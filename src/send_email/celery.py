import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')#Имя проекта get settings from settings
app.config_from_object('django.conf:settings',namespace='CELERY')#namespace
app.autodiscover_tasks()#Автоматом подцеплять наши задачи(tasks)


app.conf.beat_schedule = {
    'send-spam-every-1-minute':{
        'task':'main.tasks.send_beat_email',
        'schedule': crontab(minute='*/1'),
    }
}