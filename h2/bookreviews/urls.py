from django.urls import path
from .views import *

urlpatterns = [
    path('', BookReviewsView.as_view()),
]
