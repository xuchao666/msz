# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'msz.union.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),

    url(r'^index/$', 'index', name='index'),
    url(r'^company/$', 'company_detail', name='company_detail'),
    url(r'^company/(?P<pk>\d+)/update/$', 'company_update', name='company_update'),
    url(r'^goods/category/$', 'category_list', name='category_list'),
    url(r'^goods/product/$', 'product_list', name='product_list'),
)
