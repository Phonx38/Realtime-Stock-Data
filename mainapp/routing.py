from django.urls import re_path
from . import consumers

websocket_urlpattens = [
    re_path(r'ws/stock/(?P<room_name>\w+)/$', consumers.StockConsumer.as_asgi())
]