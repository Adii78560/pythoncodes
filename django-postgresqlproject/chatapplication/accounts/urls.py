# accounts/urls.py
from django.urls import path

from . import views

# for creating account
# using class based view

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
