from django.views.generic import TemplateView
import re
import urllib.parse, urllib.request


class active_view(TemplateView):
    template_name = 'active_main.html'

    def get_url(self):
        place = "Isreali museon"
        query_string = urllib.parse.urlencode({"search_query": place})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return f"https://www.youtube.com/embed/{search_results[0]}"

    def get_topic(self):
        return "TOPIC..."

    def get_seat(self):
        return "YOUR COMMENT: ..."