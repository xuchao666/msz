# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView as BaseCreateView, \
    UpdateView as BaseUpdateView, ListView as BaseListView, View, DetailView as BaseDetailView
from braces.views import LoginRequiredMixin, JSONResponseMixin
from django_tables2 import SingleTableView, RequestConfig


class PagedFilterTableView(SingleTableView):
    filter_class = None
    empty_text = u"暂无数据"
    enable_page_size_config = None

    @classmethod
    def strip_dic(cls, dic):
        keys = dic.keys()
        for key in keys:
            if dic[key] and isinstance(dic[key], basestring):
                dic[key] = dic[key].strip()
        return dic

    def filter_queryset(self, queryset):
        if self.filter_class:
            data = self.strip_dic(self.request.GET.copy())
            kwargs = self.get_filter_kwargs()
            kwargs.update(queryset=queryset)
            self.filter = self.filter_class(data, **kwargs)
            queryset = self.filter.qs
        return queryset

    def get_queryset(self):
        queryset = super(PagedFilterTableView, self).get_queryset()
        return self.filter_queryset(queryset)

    def get_table(self, **kwargs):
        paginate_data = {
            "per_page": self.paginate_by or getattr(settings, 'PER_PAGE', 10),
        }
        table = super(PagedFilterTableView, self).get_table()
        table.empty_text = self.get_empty_text()
        RequestConfig(self.request, paginate=paginate_data).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(PagedFilterTableView, self).get_context_data(**kwargs)
        if self.filter_class:
            context['filter_form'] = self.filter.form
        if self.enable_page_size_config:
            context['enable_page_size_config'] = True
            context['page_values'] = self.get_page_values()
        return context

    def get_page_values(self):
        defaults = ['10', '20', '50', '100', '200', '500', '1000']
        return defaults

    def get_paginate_by(self, queryset):
        if self.enable_page_size_config:
            paginate_by = self.request.REQUEST.get('count', 10)
            self.paginate_by = paginate_by
        return self.paginate_by

    def get_filter_class(self):
        return self.filter_class

    def get_filter_kwargs(self):
        return dict()

    def get_empty_text(self):
        return self.empty_text


class RequestFormKwargsMixin(object):
    """
    CBV mixin which puts the request into the form kwargs.
    Note: Using this mixin requires you to pop the `request` kwarg
    out of the dict in the super of your form's `__init__`.
    """
    def get_form_kwargs(self):
        kwargs = super(RequestFormKwargsMixin, self).get_form_kwargs()
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"request": self.request})
        return kwargs


class CommonViewMixin(LoginRequiredMixin):
    """
    """


class CreateView(RequestFormKwargsMixin, BaseCreateView):
    """
    """
    # todo: need to improve


class UpdateView(RequestFormKwargsMixin, BaseUpdateView):
    """
    """
    # todo: need to improve


class ListView(PagedFilterTableView, BaseListView):
    """
    """
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        # if request.REQUEST.get('export', '') == 'excel':
        #     return self.render_to_excel()
        # if request.REQUEST.get('export', '') in ['1', 'true']:
        #     return self.render_to_csv()
        return super(ListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class DetailView(RequestFormKwargsMixin, BaseDetailView):
    """
    """


class BatchDeleteView(CommonViewMixin, JSONResponseMixin, View):

    success_url = None

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        queryset = self.filter_queryset(queryset)

        queryset.delete()

        return self.render_json_response(dict(
            state=True,
            redirect_url=self.get_redirect_url(),
        ))

    def post(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    get = post

    def get_queryset(self):
        ids = self.request.REQUEST.get('ids', '').split(',')
        return self.model.objects.filter(pk__in=ids)

    def filter_queryset(self, queryset):
        return queryset

    def get_redirect_url(self):
        return self.success_url


class UnionCommonView(CommonViewMixin):

    login_url = reverse_lazy('union:login')
