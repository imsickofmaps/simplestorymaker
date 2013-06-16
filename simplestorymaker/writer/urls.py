from django.conf.urls import patterns, url

from writer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^latest', views.latest, name='latest'),
    url(r'^(?P<story_id>\d+)$', views.story, name='story'),
    url(r'^new', views.new, name='new'),
)
