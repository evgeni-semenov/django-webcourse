from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from .models import *

class DrinkListView(ListView):
    model = Drink

class DrinkUpdateView(LoginRequiredMixin, UpdateView):
    model = Drink
    fields = ["name", "type_name", "alcohol_content"]
    success_url = "/"

class DrinkCreateView(LoginRequiredMixin, CreateView):
    model = Drink
    fields = ["name", "type_name", "alcohol_content"]
    success_url = "/"

class DrinkDeleteView(LoginRequiredMixin, DeleteView):
    model = Drink
    success_url = "/"

class DrinkTypeListView(ListView):
    model = DrinkType

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"
    success_message = "Registration accepted. You can now log in."
