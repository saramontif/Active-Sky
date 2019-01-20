from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# def scan(request):
#     # some = "something to see\nHi!"
#     return HttpResponse(render(request, "phone_scan.html",), content_type="text/plain")

class scan(TemplateView):
    template_name = 'phone_scan.html'

