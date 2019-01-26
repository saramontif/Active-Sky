import datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
import re
import urllib.parse, urllib.request
from core.models import Dest, Facts


class Active_view(TemplateView):
    template_name = 'active_main.html'

    def dispatch(self, request, *args, **kwargs):
        #while(True):
        #    if Dest.objects.count() == 0:
         #       return redirect(reverse('start'))
         #   else:
        self.dest0 = Dest.objects.order_by("?").first()
                # now = datetime.datetime.now()
                # if (now - self.dest0.date).time().minute < 3:
                #     Dest.objects.filter(name=self.dest0.name).delete()
                # else:
                #     break

        self.recs = self.dest0.facts_set.all()
        return super().dispatch(request, *args, **kwargs)

    def get_recs(self):
        return self.recs
        # return self.recs [rec for rec in Facts.objects.all()..prefetch_related('many_set')]

    def get_url(self):
        place = self.dest0.name
        query_string = urllib.parse.urlencode({"search_query": place})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        if search_results == []:
            return "https://www.youtube.com/embed/7iBqEknWOiU?autoplay=1"
        return f"https://www.youtube.com/embed/{search_results[0]}?autoplay=1"

    def get_topic(self):
        return self.dest0.name

    def get_recognization(self):
        str_recs = [rec.content for rec in self.recs]
        return '\n\n'.join(str_recs)  # the \n does'nt work!!!

    def is_site(self):
        print(self.dest0.is_site)
        return self.dest0.is_site

    def get_num_seat(self):
        fact = [str(rec.num_seat) for rec in self.recs]
        return '\n\n'.join(fact)

