from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .models import Todo
from django.forms import ModelForm
import datetime


# class TodoForm(forms.Form):
#     todo_text_Form = forms.CharField(max_length=160, required=True)
#     todo_deadline_Form = forms.DateField(default=timezone.now(), required=True)
#     todo_progress_Form = forms.IntegerField(default=0, required=False)

#     def clean_todo_text_Form(self):
#         data = self.cleaned_data["todo_text_Form"]
        
#         if len(data) > 160:
#             raise ValidationError(_('Invalid Text - Text longer than 160 characters'))
#         return data
    
#     def clean_todo_deadline_Form(self):
#         data = self.cleaned_data["todo_deadline_Form"]

#         if data < datetime.today():
#             raise ValidationError(_('Invalid Date - Deadline in past'))
        
#         if data > datetime.today() + datetime.timedelta(years=10):
#             raise ValidationError(_('Invalid Date - Date must be in next 10 years'))

#         return data
    
#     def clean_todo_progress_Form(self):
#         data = self.cleaned_data["todo_progress_Form"]
        
#         if data < 0 or data > 100:
#             raise ValidationError(_('Invalid Progress - Progress must be between 0 and 100'))
        
#         return data



class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_text', 'deadline', 'progress']

        def clean_todo_text_Form(self):
            data = self.cleaned_data["todo_text_Form"]
        
            if len(data) > 160:
                raise ValidationError(_('Invalid Text - Text longer than 160 characters'))
            return data
    
        def clean_deadline(self):
            data = self.cleaned_data["deadline"]

            if data < datetime.date.today():
                raise ValidationError(_('Invalid Date - Deadline in past'))
            
            if data > datetime.date.today() + datetime.timedelta(years=10):
                raise ValidationError(_('Invalid Date - Date must be in next 10 years'))

            return data
        
        def clean_progress(self):
            data = self.cleaned_data["progress"]
            
            if data < 0 or data > 100:
                raise ValidationError(_('Invalid Progress - Progress must be between 0 and 100'))
            
            return data


    