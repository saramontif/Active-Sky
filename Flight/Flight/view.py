from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from expenses.models import Expense


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def expense_detail(request, pk):
    o = get_object_or_404(Expense, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })