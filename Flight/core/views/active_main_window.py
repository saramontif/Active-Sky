from django.http import HttpResponse
from django.shortcuts import render


def active_window(request):
    # some = "Active Main window\nHi!"
    return HttpResponse(render(request, "active_main.html",), content_type="text/plain")

# def expense_detail(request, pk):
#     # o = get_object_or_404(Expense, pk=pk)
#
#     return render(request, "active_main.html",)