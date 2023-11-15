from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "myapp/index.html"
    context_object_name = "items"

class ProductDetail(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "item"

@login_required
def additem(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        disc = request.POST.get("disc")
        image = request.FILES['upload']
        seller = request.user
        item = Product(name=name,price=price,disc=disc,image=image,seller=seller)
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

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("myapp:index")

