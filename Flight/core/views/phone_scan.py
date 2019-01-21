from django import forms
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from core.views.active_main_window import get_data_from_user
from core.views.main_first_window import event
import urllib.parse as urlparse


def get_seat_from_url():
    url = request.build_absolute_uri()
    parsed = urlparse.urlparse(url)
    seat = urlparse.parse_qs(parsed.query)['def']
    return seat

class ScanForm(forms.Form):
    destination = forms.CharField(label='The destination you want to travel 👉', required=False, max_length=50)
    text = forms.CharField(label="what's your recommendation❔" ,widget=forms.Textarea, max_length=100)
    seat = get_seat_from_url()

class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):
        d = form.cleaned_data
        event()
        get_data_from_user(d)
        return redirect('phone_scan')

    def form_invalid(self, form):
        return redirect('phone_scan')
