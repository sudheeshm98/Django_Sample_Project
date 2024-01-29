
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Product

# Create your views here.

def index(request):
    return HttpResponse('Hi Dears')

def test_fun(request):
    return render(request,'test.html')

def test_fun2(request):
    return render(request,'test2.html')

def products(request):
    pdts = Product.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'products':pdts,
    }
    return HttpResponse(template.render(context,request))
