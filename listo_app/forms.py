from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'in_progress', 'completed', 'due_date', 'created_at']
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


     