from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('todo_text', 'deadline', 'progress')

        widgets = {
            
            'todo_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text (less than 160 symbols)'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control'}),
        }
