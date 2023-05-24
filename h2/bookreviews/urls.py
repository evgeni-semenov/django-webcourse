from django.urls import path
from .views import *

urlpatterns = [
    path('', BookReviewsView.as_view()),
    path('reviews/new', BookCreateView.as_view()),
    path('reviews/<int:pk>', BookUpdateView.as_view()),
]
