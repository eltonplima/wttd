# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('eventex.subscriptions.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/$', 'detail', name='detail'),
    )
