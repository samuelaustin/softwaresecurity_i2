from django.conf.urls import url

from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user),
]