from django.shortcuts import render

def home(request):
    message = "hello world"
    return render(request, "home.html", {"message":message})
