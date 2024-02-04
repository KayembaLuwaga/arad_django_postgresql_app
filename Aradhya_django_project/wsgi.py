# Aradhya_django/Aradhya_django_project/wsgi.py

# WSGI config for Aradhya_django_project project.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aradhya_django_project.settings')

application = get_wsgi_application()
