from django.conf.urls import url
from .views import get_clinic

urlpatterns = [
    url(r'^(\d+)$', get_clinic, name='clinic'),
]