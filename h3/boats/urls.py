from django.urls import path
from .views import *

urlpatterns = [
    path('', BookingListView.as_view()),
    path('bookings', BookingListView.as_view()),
    path('boats', BoatListView.as_view()),
    path('boats/new', BoatCreateView.as_view()),
    path('boats/<int:pk>/delete', BoatDeleteView.as_view()),
    path('boats/<int:pk>', BoatUpdateView.as_view()),
]
