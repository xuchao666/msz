# -*- coding: utf-8 -*-
from django.contrib.admin import site
from msz.market.models import Company, Category, Product

site.register(Company)
site.register(Category)
site.register(Product)
