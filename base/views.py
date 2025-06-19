from django.shortcuts import render,redirect
from .models import Course
from .forms import MyUserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def home(request):
    message = "hello world"
    return render(request, "home.html", {"message":message})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "base/course_list.html", {"courses": courses})

def registerUser(request):
    form = MyUserCreationForm()
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error has occured during registration.")
    
    return render(request, "base/register.html", {"form": form})
    
