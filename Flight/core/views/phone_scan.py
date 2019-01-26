from django import forms

from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import FormView

from core.models import Dest, Facts
from core.views.main_first_window import event


class ScanForm(forms.Form):
    destination = forms.CharField(label='What do you want to talk about 👉\n', required=False, max_length=50)
    is_a_tourist_site = forms.BooleanField(required=False)
    text = forms.CharField(label="what's your recommendation?", widget=forms.Textarea(attrs={'rows': 6, 'cols': 25}),
                           max_length=100)


class ScanView(FormView):
    template_name = 'phone_scan.html'
    form_class = ScanForm

    def form_valid(self, form):

        d = form.cleaned_data

        if d['destination'] == '':
            return redirect(reverse('phone_scan', args=[self.kwargs['seat']]))

        try:
            print("===================")
            print("in try")
            dest0 = Dest.objects.get(name=d['destination'])
        except:
            print("===================")
            print("in except")
            dest0 = Dest(name=d['destination'], is_site=d['is_a_tourist_site'], date=timezone.now())
            dest0.save()

        print("===================")
        print("before = in dest0")
        # dest0.date = timezone.now()
        print("===================")
        print("after = in dest0")
        # dest0.save()
        print("===================")
        print("saved it")
        fact = Facts(dest_name=dest0, content=d['text'], num_seat=self.kwargs['seat'])
        fact.save()
        print("===================")
        print("dest0")
        print(dest0)


        event()
        return redirect(reverse('phone_scan', args=[self.kwargs['seat']]))

    def form_invalid(self, form):
        return redirect(reverse('phone_scan', args=[self.kwargs['seat']]))
