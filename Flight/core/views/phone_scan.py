from django import forms

from django.views.generic import TemplateView, FormView


class ScanForm(forms.Form):
    text = forms.CharField(label='text', max_length=100)
    destination = forms.Textarea(label='destination', max_length=100)


class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):
        d = form.cleaned_data
        return d

    def form_invalid(self, form):
        assert False, form.errors


