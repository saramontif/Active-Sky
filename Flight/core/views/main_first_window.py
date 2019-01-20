from django.http import HttpResponse
from django.views.generic import TemplateView


def open_window(request):
    some = "something to see\nHi!"
    return HttpResponse(some, content_type="text/plain")

class home_view(TemplateView):
    template_name = 'first_main_html.html'


