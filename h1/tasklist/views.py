from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "tasklist/base.html"

class AboutView(TemplateView):
		template_name = "tasklist/about.html"