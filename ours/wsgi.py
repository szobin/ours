"""
WSGI config for ours project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

BASE_DIR = "/home"

sys.path.append(os.path.join(BASE_DIR, 'ours'))
sys.path.append(os.path.join(BASE_DIR, 'ours', 'ours'))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ours.settings')

application = get_wsgi_application()
