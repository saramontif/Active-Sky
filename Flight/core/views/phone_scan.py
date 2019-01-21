from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class scan(TemplateView):
    template_name = 'phone_scan.html'

