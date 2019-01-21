from django import forms
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView, FormView
from django.contrib import messages


from core.views.active_main_window import get_data_from_user
from core.views.main_first_window import event
import urllib.parse as urlparse


def get_seat_from_url():
    # url = request.build_absolute_uri()
    # parsed = urlparse.urlparse(url)
    # seat = urlparse.parse_qs(parsed.query)['def']
    # return seat
    pass

class ScanForm(forms.Form):
    destination = forms.CharField(label='The destination you want to travel 👉', required=False, max_length=50)
    is_a_tourist_site = forms.BooleanField(required=False)
    text = forms.CharField(label="what's your recommendation?",widget=forms.Textarea(attrs={'rows': 5, 'cols': 25}), max_length=100)
    seat = get_seat_from_url()

    # messages.info(request, 'Your recommendation has been sent successfully!')

    # render('ScanForm_name', message='Your recommendation has been sent successfully!')


class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):
        d = form.cleaned_data
        event()
        get_data_from_user(d)
        return redirect('phone_scan')

    def form_invalid(self, form):
        # assert False, form.error
        return redirect('phone_scan')
