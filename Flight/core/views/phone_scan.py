from django import forms


from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import FormView

from core.models import Dest, Facts
from core.views.main_first_window import event

class ScanForm(forms.Form):
    destination = forms.CharField(label='The destination you want to travel 👉\n', required=False, max_length=50)
    is_a_tourist_site = forms.BooleanField(required=False)
    text = forms.CharField(label="what's your recommendation?", widget=forms.Textarea(attrs={'rows': 6, 'cols': 25}), max_length=100)
    # seat = get_seat_from_url()




class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def bool_is_site(self, d):
        if d != '':
            return True
        return False

    def form_valid(self, form):
        d = form.cleaned_data

        if d['destination'] == '':
            dest0 = Dest.objects.get(name=d['destination'])
        else:
            dest0 = Dest(name=d['destination'], is_site=self.bool_is_site(d['is_a_tourist_site']), date=timezone.now())
            dest0.save()

        # if timezone.now().minute - dest['date'].minute < 5:
        #     pass #TODO : delete from database!!!!!!!!

        # dest['date'] = timezone.now()
        # dest0.save()

        fact = Facts(dest_name=dest0, content=d['text'], num_seat=self.kwargs['seat'])
        fact.save()

        event()
        return redirect(reverse('phone_scan', args=(self.kwargs['seat'])))

    def form_invalid(self, form):
        return redirect(reverse('phone_scan', args=(self.kwargs['seat'])))

