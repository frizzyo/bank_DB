from django.shortcuts import render

from .models import Credit, CreditType, Client
# Create your views here.

def task_1(request):
    credit = Client.objects.filter(credit__cost__gt=500000, credit__cost__lt=1000000)
    context = {'credit': credit}
    return render(request,
                  'bank/1.html',
                  context)

def task_2(request):
    credit_info = CreditType.objects.order_by('interest_rate')
    context = {'credit_info': credit_info}
    return render(request,
                  'bank/2.html',
                  context)

def task_3(request):
    credit = Credit.objects.all()
    context = {'Credit': credit}
    return render(request,
                  'bank/3.html',
                  context)