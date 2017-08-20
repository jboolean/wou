from django.conf.urls import url
from . import views


app_name = 'base'
urlpatterns = [
	url(r'^readings/(?P<slug>[0-9A-Za-z\-_]+)', views.TagDetailView.as_view(), name='tag-detail'),
	url(r'^practice/(?P<slug>[0-9A-Za-z\-_]+)', views.PracticeDetailView.as_view(), name='practice-detail'),
  url(r'^$', views.IndexView.as_view(), name='index'),
]