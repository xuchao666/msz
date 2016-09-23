# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from msz.market.views import index

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'demo_tmp.views.home', name='home'),
    # url(r'^msz/', include('msz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^i18n/setlang/$', 'django.views.i18n.set_language', name='set_language'),
    url(r'^$', index, name='index'),
    url(r'', include('msz.market.urls', namespace='market')),
)


if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

    from django.views.generic import TemplateView
    urlpatterns += patterns(
        '',
        url(r'', include('dj_kits.magicpages.urls')),
        url(r'^$', TemplateView.as_view(template_name='index.html')),
    )


if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
