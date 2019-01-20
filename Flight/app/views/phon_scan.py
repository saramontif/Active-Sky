from django.shortcuts import render


def scan(request):
    # some = "something to see\nHi!"
    return render(request, 'templates/views/phon_scan.html', {})
