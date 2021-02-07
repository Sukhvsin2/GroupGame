import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from django.core.asgi import get_asgi_application
from game.consumers import GameRoom

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupgame.settings')

application = get_asgi_application()

ws_pattern = [
    path('ws/game/<u_name>/<game_id>/', GameRoom, name='game-user')
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(URLRouter(
        ws_pattern
    ))
})