from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm   # calls methods in django forms.py
    success_url = reverse_lazy('login')   # reverse is used instead of reverse because we are using class based approach
    template_name = 'signup.html'
