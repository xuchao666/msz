# -*- coding: utf-8 -*-
from django import forms
from msz.core.forms import BaseForm
from msz.market.models import Company, Category, Product, HomePic


class CompanyForm(BaseForm):

    class Meta:
        model = Company
        fields = ('name', 'mobile', 'tel', 'image', 'description', 'address', 'manager')


class CategoryForm(BaseForm):

    class Meta:
        model = Category
        fields = ('name', 'image', 'info', 'description', 'code')


class ProductForm(BaseForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'info', 'description', 'code', 'materials', 'image')


class HomePicForm(BaseForm):

    class Meta:
        model = HomePic
        fields = ('name', 'image', 'is_active')
