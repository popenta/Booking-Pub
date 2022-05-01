from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PassChangeForm, RegisterForm, EditForm
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form":form})


@login_required
def update_profile(request):
    if request.method == "POST":
        form = EditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditForm(instance = request.user)
    
    return render(request, "registration/edit_profile.html", {"form":form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PassChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = PassChangeForm(user = request.user)
    
    return render(request, "registration/change-password.html", {"form" : form})