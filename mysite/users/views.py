from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from  django.contrib.auth.models import User

from .forms import NewUserForm
# Create your views here.

def register (request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save ()
            login(request,user)
            return redirect ('myapp:index')
    form = NewUserForm()
    context = {
        'form':form
    }
    return render (request, 'users/register.html', context)

@login_required(login_url='')
def profile(request):
    return render(request, 'users/profile.html')

def seller_profile(request, id):
    seller = User.objects.get(id=id)
    context ={
        'seller':seller
    }
    return render(request, 'users/sellerprofile.html', context)


