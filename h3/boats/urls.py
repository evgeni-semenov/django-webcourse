from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', BookingListView.as_view()),
    path('bookings', BookingListView.as_view()),
    path('bookings/new', BookingCreateView.as_view()),

    path('boats', BoatListView.as_view()),
    path('boats/new', BoatCreateView.as_view()),
    path('boats/<int:pk>/delete', BoatDeleteView.as_view()),
    path('boats/<int:pk>', BoatUpdateView.as_view()),

    path('accounts/login/', LoginView.as_view(next_page="/bookings")),
    path('logout', LogoutView.as_view(next_page="/")),
]
