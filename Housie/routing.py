from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import wsfirstapp.routing

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            wsfirstapp.routing.websocket_urlpatterns
        )
    )
})