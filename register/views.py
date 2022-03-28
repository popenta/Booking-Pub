import imp
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("")
    else:
        form = RegisterForm()
    
    return render(response, "register.html", {"form":form})