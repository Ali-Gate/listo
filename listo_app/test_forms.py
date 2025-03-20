from django import forms
from .models import TodoItem
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import CommentForm

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed', 'due_date']
        widgets = {
           'due_date': forms.DateInput(attrs={'type': 'date' , 'class': 'custom-date-input'}),
        }

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }

class TestForms(TestCase):
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid') 

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")