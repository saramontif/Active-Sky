from django import forms
from django.views.generic import TemplateView, FormView

from core.views.active_main_window import get_data_from_user


class ScanForm(forms.Form):
    destination = forms.CharField(label='destination', required=False, max_length=100)
    text = forms.CharField(label='text',widget=forms.Textarea, max_length=100)


class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):
        d = form.cleaned_data
        # return d
        get_data_from_user(d)

    def form_invalid(self, form):
        assert False, form.errors


