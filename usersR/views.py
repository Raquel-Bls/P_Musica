from django.views.generic import TemplateView
#from django.shortcuts import render
# Para que te regrese a la pagina principal de una manera mas lenta
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationFrom
from django.views import generic

# Create your views here.


class homePageview(TemplateView):
    template_name = 'home.html'

# -----------------------------------------


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
