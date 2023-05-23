from django.views.generic import ListView
from .models import *

class BookReviewsView(ListView):
    model = BookReview