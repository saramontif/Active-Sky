import datetime

from django.views.generic import TemplateView
import re
import urllib.parse, urllib.request
from core.models import Dest, Facts



class Active_view(TemplateView):
    template_name = 'active_main.html'

    def dispatch(self, request, *args, **kwargs):
        self.dest0 = Dest.objects.order_by("?").first()
        # self.recs = Facts.objects.get(dest_name=self.dest0.name)
        self.recs = [rec for rec in Facts.objects.all() if rec.dest_name == self.dest0]#self.dest.fact_set.all()
        return super().dispatch(request, *args, **kwargs)

    def get_url(self):
        place = self.dest0.name
        query_string = urllib.parse.urlencode({"search_query": place})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return f"https://www.youtube.com/embed/{search_results[0]}"

    def get_topic(self):
        return self.dest0.name

    def get_recognization(self):
        self.delete_DB()
        str_recs = [rec.content for rec in self.recs]
        return '\n\n'.join(str_recs)# the \n does'nt work!!!

    def is_site(self):
        print(self.dest0.is_site)
        return self.dest0.is_site

    def get_num_seat(self):
        fact = [str(rec.num_seat) for rec in self.recs]
        return '\n\n'.join(fact)

    def delete_DB(self):
        pass
    #     now = datetime.datetime.now()
    #     fact = [ dest  for dest in self.dest0 if (now - dest.date) > 5000]
    #     Dest.objects.exclude(pk__in=list(fact)).delete()
