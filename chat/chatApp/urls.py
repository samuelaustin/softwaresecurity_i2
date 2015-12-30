from django.conf.urls import url

from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^$', views.index, name='index'),
]