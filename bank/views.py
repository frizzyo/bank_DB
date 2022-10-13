from django.shortcuts import render

from .models import Credit, CreditType, Client
from .forms import CreditForm, CreditTypeForm, ClientForm
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

def home(request):
    credit = Credit.objects.all()
    creditinfo = CreditType.objects.all().order_by('credit_type_id')
    client = Client.objects.all().order_by('client_id')
    context = {'credit': credit, 'creditinfo': creditinfo, 'client': client}
    return render(request,
                  'bank/home.html',
                  context)

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
    else:
        form = ClientForm()
    return render(request, 'bank/client_edit.html', {'form': form})


def creditinfo_new(request):
    if request.method == "POST":
        form = CreditTypeForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
    else:
        form = CreditTypeForm()
    return render(request, 'bank/creditinfo_edit.html', {'form': form})


def credit_new(request):
    if request.method == "POST":
        form = CreditForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
    else:
        form = CreditForm()
    return render(request, 'bank/credit_edit.html', {'form': form})