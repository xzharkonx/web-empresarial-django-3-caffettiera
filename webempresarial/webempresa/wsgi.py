"""
WSGI config for webempresa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webempresa.settings')

application = get_wsgi_application()

# Para subier la página a pythonanywhere.
# Seguir el tutorial, borrar todo lo de arriba y descomentar lo de abajo.

# import os
# import sys

## path = os.path.expanduser('~/mysite')
# path = os.path.expanduser('~/webempresa/webempresa')
# if path not in sys.path:
#     sys.path.insert(0, path)
## os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# os.environ['DJANGO_SETTINGS_MODULE'] = 'webempresa.settings'
# from django.core.wsgi import get_wsgi_application
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = StaticFilesHandler(get_wsgi_application())