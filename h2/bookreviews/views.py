from django.views.generic import ListView, CreateView, UpdateView
from .models import *

class BookReviewsView(ListView):
    model = BookReview

class BookCreateView (CreateView):
    model = BookReview
    fields = ["name", "review"]
    success_url = "/"

class BookUpdateView (UpdateView):
    model = BookReview
    fields = ["name", "review"]
    success_url = "/"   