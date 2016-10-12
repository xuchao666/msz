# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic import TemplateView
from dj_kits.utils.forms import errors_to_json
from braces.views import JSONResponseMixin

from msz.core.generic import UnionCommonView, UpdateView, ListView
from msz.market.filters import CategoryFilter, ProductFilter
from msz.market.forms import CompanyForm
from msz.market.models import Company, Category, Product
from msz.market.tables import CategoryTable, ProductTable
from msz.union.forms import LoginForm


class LoginView(TemplateView, JSONResponseMixin):
    template_name = 'union/union_login.html'
    redirect_url = '/union/index/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return super(LoginView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(self.redirect_url)

    def get_redirect_to_url(self, request):
        redirect_to = request.REQUEST.get('next', '/union/index/')
        return redirect_to

    def post(self, request, *args, **kwargs):
        redirect_to = self.get_redirect_to_url(request)
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            data = dict(
                state=True,
                redirect_url=redirect_to
            )
        else:
            data = dict(
                state=False,
                error=errors_to_json(form.errors)
            )
        return self.render_json_response(data)

login = LoginView.as_view()


class LogoutView(TemplateView):

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        next_url = request.REQUEST.get('next', '') or '/union/login/'
        from django.shortcuts import redirect
        return redirect(next_url)

logout = LogoutView.as_view()


class IndexView(UnionCommonView, TemplateView):
    template_name = 'union/union.html'

index = IndexView.as_view()


class CompanyDetailView(UnionCommonView, TemplateView):
    template_name = 'union/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        return context

company_detail = CompanyDetailView.as_view()


class CompanyUpdateView(UnionCommonView, UpdateView, JSONResponseMixin):
    template_name = 'union/company_update.html'
    model = Company
    form_class = CompanyForm
    success_url = '/union/company/'

company_update = CompanyUpdateView.as_view()


class CategoryListView(UnionCommonView, ListView):
    template_name = 'union/category_list.html'
    model = Category
    filter_class = CategoryFilter
    table_class = CategoryTable

category_list = CategoryListView.as_view()


class ProductListView(UnionCommonView, ListView):
    template_name = 'union/product_list.html'
    model = Product
    filter_class = ProductFilter
    table_class = ProductTable

product_list = ProductListView.as_view()
