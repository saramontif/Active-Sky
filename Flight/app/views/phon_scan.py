from django.shortcuts import render
from django.http import HttpResponse


def scan(request):
    # some = "something to see\nHi!"
    return render(request, 'templates/Flight/phon_scan.html', {})

# def phon_scan(request):
#     return render(request, 'app/phon_scan.html', {})