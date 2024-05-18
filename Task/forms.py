from django import forms
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
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'My Task'}),
            'deadline': forms.TextInput(attrs={'id': 'id_deadline','autocomplete':'off'}),  
            'time': forms.TextInput(attrs={'id': 'clockpicker','autocomplete':"off"}), 
        }
    def clean(self):
        cleaned_data = super().clean()
        time = cleaned_data.get('time')
        deadline = cleaned_data.get('deadline')

        if time and not deadline:
            self.add_error('deadline', 'Date is required if time is provided.')

        