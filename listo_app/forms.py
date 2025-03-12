from django import forms
from .models import TodoItem
from django.contrib.auth.models import User

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed', 'due_date']
        widgets = {
           'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }

     