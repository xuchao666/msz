# -*- coding: utf-8 -*-
from django.shortcuts import render
from msz.market.models import Category, Company, HomePic, Product


def __initial_base_data():
    categories = Category.objects.filter()
    try:
        company = Company.objects.first()
    except:
        company = None

    context = dict(
        categories=categories,
        company=company,
    )
    return context


def index(request):
    context = __initial_base_data()
    pics = HomePic.objects.all()[:3]
    context.update(dict(pics=pics))
    return render(request, 'market/index.html', context)


def category_info(request, pk):
    context = __initial_base_data()
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context.update(dict(category=category, products=products))
    return render(request, 'market/category.html', context=context)


def buy(request):
    context = __initial_base_data()
    return render(request, 'market/buy.html', context=context)
