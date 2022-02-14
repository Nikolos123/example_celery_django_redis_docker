from django.core.mail import send_mail


def send(user_email):
    for i in range(10):
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать Вам много спама.',
            'django.celery.redis@gmail.com',
            [user_email],
            fail_silently=False
        )

#Qwert123$