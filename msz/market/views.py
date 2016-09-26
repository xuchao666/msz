# -*- coding: utf-8 -*-
from django.shortcuts import render
from msz.market.models import Category, Company


def __initial_base_data():
    categories = Category.objects.filter()
    try:
        company = Company.objects.first()
    except:
        company = None
    print company
    context = dict(
        categories=categories,
        company=company
    )
    return context


def index(request):
    context = __initial_base_data()
    return render(request, 'market/index.html', context)


def category_info(request, pk):
    category = Category.objects.get(pk=pk)
    context = dict(category=category)
    return render(request, 'market/category.html', context=context)
