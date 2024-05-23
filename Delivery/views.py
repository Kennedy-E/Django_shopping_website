from django.shortcuts import render
from django.http import HttpResponse
from .models import Goods

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Hello Esther</h1>')

def home(request):
    return render(request, 'Delivery/home.html')