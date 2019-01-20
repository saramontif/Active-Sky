from django.shortcuts import render
from django.http import HttpResponse

def phon_scan(request):
    return render(request, 'app/phon_scan.html', {})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

