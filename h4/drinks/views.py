from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import *

class DrinkListView(ListView):
    model = Drink

class DrinkUpdateView(UpdateView):
    model = Drink
    fields = ["name", "type_name", "alcohol_content"]
    success_url = "/"

class DrinkCreateView(CreateView):
    model = Drink
    fields = ["name", "type_name", "alcohol_content"]
    success_url = "/"

class DrinkDeleteView(DeleteView):
    model = Drink
    success_url = "/"

class DrinkTypeListView(ListView):
    model = DrinkType
