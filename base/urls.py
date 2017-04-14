from django.conf.urls import url
from . import views


app_name = 'base'
urlpatterns = [
	url(r'^readings/(?P<slug>[0-9A-Za-z\-_]+)', views.ReadingDetailView.as_view(), name='readings-tag'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]