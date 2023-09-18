# Create your views here.
# Blog/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')


def fotter(request):
    return render(request, 'fotter.html')


def contact(request):
    return render(request, 'contact.html') 


def features(request):
    return render(request, 'features.html')


def faq(request):
    return render(request, 'faq.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blogcontent(request):
    return render(request, 'blogcontent.html')

