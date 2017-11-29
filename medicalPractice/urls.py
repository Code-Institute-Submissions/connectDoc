from django.conf.urls import url, include
from .views import all_doctors, do_search, practice_details

urlpatterns = [
    url(r'^$', all_doctors, name='medicalPractice'),
    url(r'^search/', do_search, name='search'),
    url(r'^(\d+)$', practice_details, name='practice_details'),
]