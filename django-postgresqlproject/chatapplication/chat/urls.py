# chat/urls.py
from django.urls import path, re_path   # normal path and regular expression path

from . import views   # . for current directory

urlpatterns = [
    path('home/', views.home, name='index'),   # after login page whenever browser request home/
    re_path(r'(?P<room_name>[^/]+)/$', views.room, name='room'),  # after entering room in home it will load room

    # html with room name
]
