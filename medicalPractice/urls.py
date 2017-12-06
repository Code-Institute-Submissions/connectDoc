from django.conf.urls import url, include
from .views import all_doctors, practice_details
from booking.views import booking
from checkout import urls as checkout_urls

urlpatterns = [
    url(r'^$', all_doctors, name='medicalPractice'),
    url(r'^(\d+)$', practice_details, name='practice_details'),
    url(r'^(\d+)/booking$', booking, name='booking'),
    url(r'^(\d+)/booking/checkout', include(checkout_urls)),
]