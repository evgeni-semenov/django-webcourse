from django.urls import path
from .views import *

urlpatterns = [
    path('', DrinkListView.as_view()),
    path('drinks/', DrinkListView.as_view()),
    path('drinks/<int:pk>/edit', DrinkUpdateView.as_view()),
    path('drinks/new/', DrinkCreateView.as_view()),
    path('types', DrinkTypeListView.as_view()),
]
