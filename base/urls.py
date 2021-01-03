from django.conf.urls import url
from . import views
from six import python_2_unicode_compatible


app_name = 'base'
urlpatterns = [
	url(r'^readings/(?P<slug>[0-9A-Za-z\-_]+)', views.TagDetailView.as_view(), name='tag-detail'),
	url(r'^practice/(?P<slug>[0-9A-Za-z\-_]+)', views.PracticeDetailView.as_view(), name='practice-detail'),
  url(r'^mailing-list/join', views.MailingListJoinView.as_view(), name='mailing-list-join'),
  url(r'^pastevents', views.PastView.as_view(), name='past-events'),
  url(r'^$', views.IndexView.as_view(), name='index'),
]