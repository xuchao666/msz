# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'msz.market.views',
    url(r'^sss/$', 'index', name='indexs'),
)
