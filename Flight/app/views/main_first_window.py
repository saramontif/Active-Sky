from django.http import HttpResponse


def open_window(request):
    some = "something to see\nHi!"
    return HttpResponse(some, content_type="text/plain")




