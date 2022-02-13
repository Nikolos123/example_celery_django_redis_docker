from time import time

# Create your views here.
from django.views.generic import CreateView

from main.forms import ContactForm
from main.models import Contact
from .tasks import send_spam_email

class ContactView(CreateView):
    """отображение формы подписки на email"""
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact/contact.html'
    
    def form_valid(self, form):
        form.save()
        t0 = time()
        # send(form.instance.email)
        # print(time() - t0)

        send_spam_email.delay(form.instance.email)# stark task - не ждем ответа #Передаем конкретное поле
        print(time() - t0)
        #Пока функция не завершиться мы будем ждать
        #Такие задачи нужно выполнять через celery
        return super(ContactView, self).form_valid(form)