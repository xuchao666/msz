# -*- coding: utf-8 -*-
from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic import TemplateView
from dj_kits.utils.forms import errors_to_json
from braces.views import LoginRequiredMixin, JSONResponseMixin
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
        next_url = request.REQUEST.get('next', '') or '/'
        from django.shortcuts import redirect
        return redirect(next_url)

logout = LogoutView.as_view()


class IndexView(TemplateView):
    template_name = 'union/union.html'

index = IndexView.as_view()
