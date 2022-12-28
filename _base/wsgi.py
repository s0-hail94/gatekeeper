"""
WSGI config for Gatekeeper project.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_base.settings')

application = get_wsgi_application()
