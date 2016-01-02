from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^register/$', views.Register),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]