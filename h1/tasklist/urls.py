from django.urls import path
from .views import *

urlpatterns = [
		path('', HomePageView.as_view()),
        path('about', AboutView.as_view()),
        path('peruna', PerunaView.as_view()),
        path('tasks', TaskListView.as_view()),
]