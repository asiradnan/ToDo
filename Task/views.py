from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import TaskForm
from .models import Task
def home(request):
    tasks=Task.objects.all()
    return render(request,"ToDo/home.html",{"tasks":tasks})

def addTask(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            x=form.save(commit=False)
            x.user=request.user
            x.save()
            return HttpResponseRedirect("/")
    else:
        form = TaskForm()
    return render(request,"task/task.html",{"form":form})

def delete(request,id):
    task=Task.objects.filter(id=id)
    task.delete()
    return HttpResponseRedirect("/")