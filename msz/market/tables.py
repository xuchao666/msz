# -*- coding: utf-8 -*-
from django_tables2 import tables

from msz.market.models import Category, Product, HomePic


class CategoryTable(tables.Table):

    class Meta:
        model = Category


class ProductTable(tables.Table):

    class Meta:
        model = Product


class HomePicTable(tables.Table):

    class Meta:
        model = HomePic
