from django.conf.urls import url
from .views import booking

urlpatterns = [
    # url(r'^(\d+)$', practice_details, name='practice_details'),
    url(r'^$', booking, name='book_appointment'),
]