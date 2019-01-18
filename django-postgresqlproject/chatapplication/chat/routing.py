# chat/routing.py

# it is similar to urls.py in django
# here we are providing web socket path requested by server

from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
