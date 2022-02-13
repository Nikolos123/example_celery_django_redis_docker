
from django.urls import path

from main.views import ContactView

app_name = 'main'

urlpatterns = [
    path('', ContactView.as_view(),name="contact" ),
]
