from django.views.generic import TemplateView, ListView
from .models import *

class HomePageView(TemplateView):
    template_name = "tasklist/base.html"

class AboutView(TemplateView):
    template_name = "tasklist/about.html"
                
class PerunaView(TemplateView):
    template_name = "tasklist/peruna.html"

class TaskListView(ListView):
    model = Task
