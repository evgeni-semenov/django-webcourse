from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', DrinkListView.as_view()),
    path('drinks/', DrinkListView.as_view()),
    path('drinks/<int:pk>/edit', DrinkUpdateView.as_view()),
    path('drinks/new/', DrinkCreateView.as_view()),

    path('types', DrinkTypeListView.as_view()),
    
    path('accounts/login/', LoginView.as_view(next_page="/")),
    path('logout', LogoutView.as_view(next_page="/")),

    path('register', RegisterView.as_view()),
]
