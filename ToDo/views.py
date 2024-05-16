from django.shortcuts import render

def home(request):
    return render(request,"ToDo/home.html")