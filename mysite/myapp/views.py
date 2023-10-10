from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.


def index(request):

    items = Product.objects.all()
    context = {
        'items':items
    }
    return render(request, "myapp/index.html", context)


def Detail (request,id):

    item = Product.objects.get(id=id)
    context = {
        'item': item
    }

    return render(request, "myapp/detail.html", context)

