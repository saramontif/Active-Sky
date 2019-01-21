from django import forms


from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from core.views.active_main_window import get_data_from_user
from core.views.main_first_window import event

class ScanForm(forms.Form):
    destination = forms.CharField(label='The destination you want to travel 👉\n', required=False, max_length=50)
    is_a_tourist_site = forms.BooleanField(required=False)
    text = forms.CharField(label="what's your recommendation?", widget=forms.Textarea(attrs={'rows': 6, 'cols': 25}), max_length=100)
    # seat = get_seat_from_url()




class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):
        d = form.cleaned_data
        d['seat'] = self.kwargs['seat']
        event()
        get_data_from_user(d)
        return redirect(reverse('phone_scan', args=(self.kwargs['seat'],)))

    def form_invalid(self, form):
        d = form.cleaned_data
        d['seat'] = self.kwargs['seat']
        return redirect(reverse('phone_scan', args=(self.kwargs['seat'],)))

