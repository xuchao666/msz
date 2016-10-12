# -*- coding: utf-8 -*-
import re
import cStringIO
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Reset, Submit, Layout, Div, HTML
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Q
from django.forms import ModelMultipleChoiceField
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
import django_filters
from dj_kits.utils.forms import FormBaseMixin
from django import forms
import operator


class BaseForm(FormBaseMixin, forms.ModelForm):
    i18n_fields = []
    fields_widget_with_form = []

    form_class = 'form-horizontal'
    form_inputs = [Submit('submit', _(u'保存')),
                   Reset('reset', _(u'重置'))]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BaseForm, self).__init__(*args, **kwargs)

        lang = self.get_lang()
        if lang:
            for field in self.i18n_fields:
                self.fields.pop('%s_%s' % (field, lang), None)

        for field in self.fields_widget_with_form:
            self.fields[field].widget.form = self

    def is_edit(self):
        return self.instance.pk is not None

    def get_lang(self):
        return getattr(self.request, 'LANGUAGE_CODE', '').replace('-', '_')


class BaseFilterForm(FormBaseMixin, forms.Form):
    form_class = 'form-horizontal'
    form_method = 'get'

    def __init__(self, *args, **kwargs):
        super(BaseFilterForm, self).__init__(*args, **kwargs)
        self.keys = self.fields.keys()
        for k, v in self.fields.items():
            v.help_text = False

    def get_layout(self, helper):
        layout = Layout(
            Div(*self.keys, css_class="inline-group"),
            FormActions(Submit('submit', _(u'查询'))),
            Div(HTML("""<span class="search-slider-btn"></span>"""), css_class="search-slider")
        )
        return layout


class TemplateRenderFieldMixin(object):

    template = None

    def __init__(self, *args, **kwargs):
        template = kwargs.pop('template', None)
        if template:
            self.template = template

        if not self.template:
            raise Exception("template is required.")

        super(TemplateRenderFieldMixin, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        template = kwargs.pop('template', None)
        if template:
            self.template = template

        field = super(TemplateRenderFieldMixin, self).render(*args, **kwargs)
        return render_to_string(self.template, {'field': field, 'widget': self})


class TemplateRenderSelect(TemplateRenderFieldMixin, forms.Select):
    """ """


class TemplateRenderSelectMultiple(TemplateRenderFieldMixin, forms.SelectMultiple):
    """ """


class TemplateRenderClearableFileInput(TemplateRenderFieldMixin, forms.FileInput):
    """ """
    def value_from_datadict(self, data, files, name):
        val = files.get(name, None) or data.get(name, None)
        if isinstance(val, (basestring, unicode)) and val:
            file_name = data.get('name', 'logo')
            img_str = re.search(r'base64,(.*)', val).group(1)
            temp_img = cStringIO.StringIO(img_str.decode('base64'))
            val = SimpleUploadedFile(file_name, temp_img.read())
        return val

