from django.http import HttpResponse

from django.views.generic import TemplateView


def active_window(request):
    some = "Active Main window\nHi!"
    return HttpResponse(some, content_type="text/plain")

class active_view(TemplateView):
    template_name = 'active_main.html'
