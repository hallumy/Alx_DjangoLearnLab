from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/register.html', {"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST,get("email")
        request.user.save()
        return redirect("profile")
    
    return render(request, "auth/profile", {"user": request.user})
    
def home(request):
    return render(request, "blog/home.html")

from django.shortcuts import render

def posts(request):
    return render(request, "blog/posts.html")

        

