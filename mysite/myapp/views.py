from django.shortcuts import render,redirect
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

def additem(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        disc = request.POST.get("disc")
        image = request.FILES['upload']
        item = Product(name=name,price=price,disc=disc,image=image)
        item.save()
    return render(request, "myapp/additem.html")

def updateitem(request,id):
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.disc = request.POST.get("disc")
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect("http://127.0.0.1:8000/")

    context = {
        'item': item
    }

    return render(request,"myapp/updateitem.html", context)

def deleteitem(request, id):
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("http://127.0.0.1:8000/")

    context = {
        'item': item
    }
    return render(request, "myapp/delete.html", context)


