from django.http import HttpResponse


def active_window(request):
    some = "Active Main window\nHi!"
    return HttpResponse(some, content_type="text/plain")

