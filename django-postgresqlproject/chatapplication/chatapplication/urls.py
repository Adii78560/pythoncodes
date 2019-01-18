# my_project/urls.py
from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView  # TemplateView is a generic class-based view that helps
# developers create a view for a specific template


urlpatterns = [
    path('admin/', admin.site.urls),   # localhost/admin
    path('accounts/', include('accounts.urls')),  # for signup
    path('accounts/', include('django.contrib.auth.urls')),   # for login
    path('chat/', include('chat.urls')),  # login and sign in page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # home page after login

]
