from django import forms
from django.shortcuts import redirect
from .models import Task
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.fields:
            self.fields['password1'].help_text = None
        if 'password2' in self.fields:
            self.fields['password2'].help_text = None

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["name","deadline","time"]