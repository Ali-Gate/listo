from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed', 'due_date']
        widgets = {
           'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


     