# -*- coding: utf-8 -*-
from django import forms
from msz.core.forms import BaseForm
from msz.market.models import Company


class CompanyForm(BaseForm):

    class Meta:
        model = Company
        fields = ('name', 'mobile', 'tel', 'image', 'description', 'address', 'manager')
