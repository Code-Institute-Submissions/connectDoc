"""connectDOC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_urls
from .settings import MEDIA_ROOT
from django.views import static
from accounts.views import get_index
from medicalPractice import urls as urls_medicalPractice
from medicalPractice.views import all_doctors
from checkout import urls as urls_checkout
from booking import urls as urls_booking
from search import urls as urls_search
from search.views import do_search



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_doctors, name='index'),
    url(r'^accounts/' ,include(accounts_urls)),
    url(r'^doctor/', include(urls_medicalPractice)),
    url(r'^search/', do_search, name='search'),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),

]