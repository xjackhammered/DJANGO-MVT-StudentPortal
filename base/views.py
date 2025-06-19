from django.shortcuts import render,redirect
from .models import Course
from .forms import MyUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

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
    
def logoutUser(request):
    logout(request)
    return redirect("home")

def loginPage(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist.")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Email or password is incorrect.")
    
    return render(request, "base/login.html")