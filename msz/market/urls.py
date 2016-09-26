# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'msz.market.views',
    url(r'^category/(?P<pk>\d+)/$', 'category_info', name='category_info'),
)
