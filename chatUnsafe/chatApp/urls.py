from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register/$', views.Register),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^$', views.index, name='index'),
]