from django.conf.urls import patterns, url

from swevoteapp import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	url(r'^vote/$', views.detail, name='detail'),
	url(r'^vote/voting', views.vote, name='vote'),
	url(r'^vote/thanks', views.thanks, name='thanks'),
	# ex: /polls/5/
	#url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	# ex: /polls/5/results/
	#url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	#url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
