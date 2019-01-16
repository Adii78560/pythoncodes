# my_project/urls.py
from django.contrib import admin
from django.urls import path, include,re_path

from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #re_path(r'^accounts/(?P[0-9])/$', )
]