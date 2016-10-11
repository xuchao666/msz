# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from dj_kits.utils.forms import FormBaseMixin
from django.contrib import auth


class LoginForm(FormBaseMixin, forms.Form):
    username = forms.CharField(required=True, label=_(u"用户名"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_(u"密码"))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == "" or username.isspace():
            raise forms.ValidationError(u"用户名不能为空")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password == "" or password.isspace():
            raise forms.ValidationError(u"密码不能为空")
        if len(password) < 6:
            raise forms.ValidationError(u"请输入一个不小于6位的密码！")
        return password

    def clean(self):
        cleaned_data = self.cleaned_data
        if not self.errors:
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            kw = dict(username=username, password=password)
            user = auth.authenticate(**kw)
            if user is not None:
                if user.is_active:
                    auth.login(self.request, user)
                else:
                    self.add_error('username', u"该用户已被禁止登陆！")
            else:
                self.add_error('username', u"用户名或密码不正确，请重试！")
        return cleaned_data
