from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from .forms import TaskForm
from .models import Task
def home(request):
    if request.user.is_authenticated:
        tasks=Task.objects.filter(user=request.user)
    else:
        tasks=None
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

def completed(request,id):
    task=get_object_or_404(Task, id=id)
    task.completed=not task.completed
    task.save()
    return HttpResponseRedirect("/")

def update(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form=TaskForm(instance=task)
    return render(request,"task/task.html",{"form":form})
