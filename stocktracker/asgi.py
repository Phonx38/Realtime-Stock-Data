"""
ASGI config for stocktracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from mainapp.routing import  websocket_urlpattens
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocktracker.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)
  "websocket": AuthMiddlewareStack(
      URLRouter(
          websocket_urlpattens
      )
  )
})
