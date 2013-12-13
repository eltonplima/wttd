# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'home', name='home'),
    )
