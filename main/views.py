from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'main/index.html',)

def cus_list(request):
    items = Item.objects.all()
    return render(request, 'main/cus_table.html', {'items': items, 'text': 'العهدة'})

def req_list(request):
    requests = Reqeust.objects.all()
    return render(request, 'main/req_table.html', {'items': requests, 'text': 'الطلبات'})