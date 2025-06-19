from django.shortcuts import render
from .models import Course

def home(request):
    message = "hello world"
    return render(request, "home.html", {"message":message})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "base/course_list.html", {"courses": courses})