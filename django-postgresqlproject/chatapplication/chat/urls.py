# chat/urls.py
from django.urls import path, re_path   # normal path and regular expression path
from django.contrib.auth.views import login
from . import views   # . for current directory

urlpatterns = [
    #path('login/',views.login, name='login'),

    path('home/', views.home, name='index'),   # after login page whenever browser request home/
    path('login/', login,{'template_name': 'registration/login.html'}),
    re_path(r'(?P<room_name>[^/]+)/$', views.room, name='room'),  # after entering room in home it will load room

    # html with room name
]
