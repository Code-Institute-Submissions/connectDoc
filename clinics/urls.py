from django.conf.urls import url
from .views import get_clinic, all_clinics

urlpatterns = [
    url(r'^$', all_clinics, name='all_clinics'),
    url(r'^(\d+)$', get_clinic, name='clinic'),
]