"""
WSGI config for webplayground project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Añadir la carpeta padre de esta (webplayground_project) al sys.path
current_path = os.path.dirname(os.path.abspath(__file__))  # ruta a webplayground/
project_path = os.path.dirname(current_path)                # ruta a webplayground_project/
sys.path.append(project_path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webplayground.settings')

application = get_wsgi_application()
