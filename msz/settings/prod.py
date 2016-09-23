# -*- coding: utf-8 -*-
from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


CACHES = {
    'default': env.cache_url()
}


COMPRESS_OFFLINE = True


DATABASES = {
    'default': env.db_url()
}


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# Examples: "http://media.lawrence.com/media/",
# "http://example.com/media/""
MEDIA_URL = env('MEDIA_URL')


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = env('STATIC_URL')

# tracker id for piwik
PIWIK_TRACKER_ID = env('PIWIK_TRACKER_ID', default='')


# If you set this to True, supervisor will be used.
USE_SUPERVISOR = env.bool('USE_SUPERVISOR', default=False)

if USE_SUPERVISOR:

    INSTALLED_APPS += ('djsupervisor', )

    def get_virtualenv():
        import sys
        if hasattr(sys, 'real_prefix'):
            virtualenv = sys.prefix
        else:
            virtualenv = None
        return virtualenv

    VIRTUALENV = get_virtualenv()

    PROJECT_VAR_DIR = root('../var/', ensure=True)
    PROJECT_LOG_DIR = root('../var/log/', ensure=True)
    PROJECT_RUN_DIR = root('../var/run/', ensure=True)

    UWSGI_SOCKET = env.list('UWSGI_SOCKET', default=['127.0.0.1:8080'])
    UWSGI_LIMIT_AS = env.int('UWSGI_LIMIT_AS', default=0)
