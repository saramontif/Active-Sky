from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from core.views.active_main_window import get_data_from_user
from core.views.main_first_window import event


class ScanForm(forms.Form):
    destination = forms.CharField(label='The destination you want to travel 👉', required=False, max_length=50)
    is_a_tourist_site = forms.BooleanField()
    text = forms.CharField(label="what's your recommendation?",widget=forms.Textarea(attrs={'rows': 6, 'cols': 27}), max_length=100)



class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):
        d = form.cleaned_data
        event()
        get_data_from_user(d)
        return redirect('phone_scan/')

    def form_invalid(self, form):
        # assert False, form.error
        return redirect('phone_scan/')
