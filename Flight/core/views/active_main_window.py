from django.views.generic import TemplateView
import re
import urllib.parse, urllib.request

temp = 'active_main.html' #'first_main_html.html'
destination = ""
recommendations = []
def get_data_from_user(d):
    # global temp
    # temp = 'active_main.html'

    global destination

    if d['destination'] != '':
        destination = d['destination']
        recommendations.clear()

    recommendations.append("SEAT __:    " + d['text'])


class Active_view(TemplateView):
    template_name = temp

    def get_url(self):
        place = destination
        query_string = urllib.parse.urlencode({"search_query": place})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return f"https://www.youtube.com/embed/{search_results[0]}"

    def get_topic(self):
        return destination

    # def get_seat(self):
    #     return "SEAT __:    "


    def get_recognization(self):
        return '\n\n'.join(recommendations) # the \n does'nt work!!!