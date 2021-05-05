"""
WSGI config for vancouvar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('<PATH_TO_MY_DJANGO_PROJECT>/vancouvar')

# add the virtualenv site-packages path to the sys.path
sys.path.append('<PATH_TO_VIRTUALENV>/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vancouvar.settings')

application = get_wsgi_application()

from helloworld.wsgi import HelloWorldApplication

application = HelloWorldApplication(application)