from django.shortcuts import render
from django.http import HttpResponse


def scan(request):
    some = "something to see\nHi!"
    return HttpResponse(some, content_type="text/plain")

# def phon_scan(request):
#     return render(request, 'app/phon_scan.html', {})