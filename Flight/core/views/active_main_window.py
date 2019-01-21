from django.http import HttpResponse

from django.views.generic import TemplateView


class active_view(TemplateView):
    template_name = 'active_main.html'
