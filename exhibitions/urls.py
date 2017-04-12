from django.conf.urls import url
from . import views


app_name = 'exhibitions'
urlpatterns = [
	url(r'^(?P<slug>[0-9A-Za-z\-_]+)/past', views.PastView.as_view(), name='past'),
    url(r'^(?P<slug>[0-9A-Za-z\-_]+)/$', views.IndexView.as_view(), name='detail'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
]