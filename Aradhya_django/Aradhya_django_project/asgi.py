# Aradhya_django/Aradhya_django_project/asgi.py

# ASGI config for Aradhya_django_project project.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aradhya_django_project.settings')

application = get_asgi_application()
