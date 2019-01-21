from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

flag = False

def event():
    global flag
    flag = True

def get_flag():
    return flag


class HomeView(TemplateView):
    template_name = 'first_main_html.html'


# def flag_view(request):
#     return JsonResponse({'flag': get_flag()})


class FlagView(View):
    def get(self, request, *args, **kwargs):
        flag0 = get_flag()
        return JsonResponse({'flag': flag0})
