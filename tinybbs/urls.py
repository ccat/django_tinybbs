from django.conf.urls import patterns, include, url

from django.http import Http404

from views import *

urlpatterns = patterns('',
    url(r'^$', show_index,name="tinybbs_show_index"),
    url(r'^(?P<url>.*)$', show_topic,name="tinybbs_show_topic"),
)
