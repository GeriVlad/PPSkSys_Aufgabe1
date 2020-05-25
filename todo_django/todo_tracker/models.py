from django.db import models
from datetime import date

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=160)
    deadline = models.DateField(default=date.today, null=True)
    progress = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.todo_text
