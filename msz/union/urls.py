# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'msz.union.views',
    url(r'^/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)
