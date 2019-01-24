# chatapplication/routing.py
from channels.auth import AuthMiddlewareStack   # in Channels supports standard Django authentication, where the user
# details are stored in the session

from channels.routing import ProtocolTypeRouter, URLRouter

# ProtocolTypeRouter : lets you dispatch to one of a number of other ASGI applications based on the type value
# present in the scope

import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
