from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from .forms import TaskForm
from .models import Task
from allauth.account.models import EmailAddress
from django.contrib.auth.forms import PasswordResetForm,PasswordChangeForm
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash


def profile(request):
    if request.method == 'POST':
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
        elif 'password_change' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
            else:
                print(password_form.error_messages)
                print(request.POST)
        else:
            print(request.POST)

    context = {
        'email_addresses': EmailAddress.objects.filter(user=request.user),
        'form':PasswordChangeForm(user=request.user)
    }
    return render(request, 'task/profile.html', context)


def home(request):
    section = request.GET.get('section', 'todaylist')
    if request.user.is_authenticated:
        tasks=Task.objects.filter(user=request.user)
    else:
        tasks=None
    current_timezone = timezone.get_current_timezone()
    today_in_timezone = timezone.localtime(timezone.now(), current_timezone).date()
    return render(request,"ToDo/home.html",{"tasks":tasks,"today":today_in_timezone,"section":section})

   
def addTask(request):
    section = request.GET.get('section', 'todaylist')  
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            x=form.save(commit=False)
            x.user=request.user
            x.save()
            return redirect(f"{reverse('Task:home')}?section={section}")
    else:
        form = TaskForm()
    return render(request,"task/task.html",{"form":form})

def delete(request, id):
    section = request.GET.get('section', 'todaylist')
    task=get_object_or_404(Task,id=id)
    task.delete()
    return redirect(f"{reverse('Task:home')}?section={section}")

def complete_task(request, id):
    section = request.GET.get('section', 'todaylist')
    task=get_object_or_404(Task,id=id)
    task.completed=not task.completed
    task.save()
    return redirect(f"{reverse('Task:home')}?section={section}")

def update(request,id):
    section = request.GET.get('section', 'todaylist')  
    task=get_object_or_404(Task,id=id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"{reverse('Task:home')}?section={section}")
    form=TaskForm(instance=task)
    return render(request, "task/task.html", {"form": form, "section": section,"id":id})
