from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator

# Create your models here.

class Todo(models.Model):
    todo_text = models.CharField(max_length=160)
    deadline = models.DateField(default=date.today, null=True)
    progress = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], null=True)

    def __str__(self):
        return self.todo_text
