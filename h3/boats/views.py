from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class BoatListView(ListView):
    model = Boat

class BoatUpdateView(UpdateView):
    model = Boat
    fields = ["name", "make", "engine_hp", "owner_name"]
    success_url = "/"

class BoatCreateView(CreateView):
    model = Boat
    fields = ["name", "make", "engine_hp", "owner_name"]
    success_url = "/"

class BoatDeleteView(DeleteView):
    model = Boat
    success_url = "/"

class BookingListView(ListView):
    model = Booking

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ["booking_date", "boat", "lessor_name"]
    success_url = "/"

