"""
WSGI config for hermes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/theraasch/apps_wsgi')

sys.path.append('/home/theraasch/apps_wsgi/hermes')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hermes.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
