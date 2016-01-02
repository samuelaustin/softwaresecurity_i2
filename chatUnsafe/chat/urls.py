from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^chatApp/', include('chatApp.urls')),
]
