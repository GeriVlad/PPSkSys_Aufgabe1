from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

#TODO creat function that shortens todo_text for display __str__ 

class Todo(models.Model):
    #added_on triggers when object is created
    added_on = models.DateField(auto_now_add=True)
    #last_modified updated on 
    last_modified = models.DateTimeField(auto_now=True)
    #Todo Text max 160 chars
    todo_text = models.CharField(max_length=160)
    #Deadline - defaults to today
    deadline = models.DateField(default=datetime.date)
    #Progress - integer between 0 and 100
    progress = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    def __str__(self):
        return self.todo_text
    def deadline_soon(self):
        return self.deadline >= timezone.now() + datetime.timedelta(days=7)