from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from .forms import TaskForm
from .models import Task
from allauth.account.models import EmailAddress
from django.contrib.auth.forms import PasswordResetForm

def profile(request):
    if request.method == 'POST':
        print("called")
        if 'action_reset_password' in request.POST:
            email = request.POST.get('email')
            form = PasswordResetForm({'email': email})
            if form.is_valid():
                form.save(request=request)

        elif 'action_send' in request.POST:
            email = request.POST.get('email')
            email_address = EmailAddress.objects.filter(email=email, user=request.user).first()
            if email_address:
                email_address.send_confirmation(request)

        elif 'action_remove' in request.POST:
            print("We are here")
            email = request.POST.get('email')
            email_address = EmailAddress.objects.filter(email=email, user=request.user).first()
            print(email_address)
            if email_address:
                print(email_address.delete())
        elif 'action_add' in request.POST:
            new_email = request.POST.get('email')
            if new_email:
                email_address, created = EmailAddress.objects.get_or_create(user=request.user, email=new_email)
                if created:
                    email_address.send_confirmation(request)

    context = {
        'email_addresses': EmailAddress.objects.filter(user=request.user),
    }
    return render(request, 'task/profile.html', context)


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
