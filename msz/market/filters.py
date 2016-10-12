# -*- coding:utf-8 -*-
import django_filters
from msz.market.models import Category, Product


class CategoryFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(name="code", lookup_type="icontains")
    name = django_filters.CharFilter(name="name", lookup_type="icontains")

    class Meta:
        model = Category
        fields = ('code', 'name')


class ProductFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(name="code", lookup_type="icontains")
    name = django_filters.CharFilter(name="name", lookup_type="icontains")

    class Meta:
        model = Product
        fields = ('name', 'code')
