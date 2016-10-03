from django.conf.urls import url
from . import views


app_name = 'base'
urlpatterns = [
    url(r'^(?P<slug>[0-9A-Za-z\-_]+)/$', views.IndexView.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]