from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Todo
from .forms import TodoForm
# import .views

def create_Todo(todo_text, deadline, progress):
    return Todo.objects.create(todo_text=todo_text, deadline=deadline, progress=progress)

good_todo = Todo.objects.create(todo_text = "testing", deadline = datetime.date.today(), progress = 0)

class TodoModelTests(TestCase):
    def test_todo_text_too_long(self):
        text = "This text will be very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long"
        test_todo = Todo(todo_text=text)
        self.assertIs(test_todo.save(), None)

    
    # def test_TodoForm_correct_inputs(self):
    #     TodoForm.

class TodoOverviewTests(TestCase):
    def test_no_todos(self):
        response = self.client.get(reverse('todos:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Todo's are available")
        self.assertQuerysetEqual(response.context['latest_todo_list'])


class saving_Todos(TestCase):
    def test_good_todo(self):
        good_todo.save()
        self.assertContains(Todo.objects.all(), good_todo)
        