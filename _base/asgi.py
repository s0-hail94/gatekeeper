"""
ASGI config for Gatekeeper project.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_base.settings')

application = get_asgi_application()
