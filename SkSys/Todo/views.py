from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def index(request):
    latest_Todo_list = Todo.objects.order_by('-added_on')[:5]
    output = ', <br/>    '.join([t.todo_text for t in latest_Todo_list])
    return HttpResponse(output)

def detail(request, Todo_id):
    return HttpResponse("You're looking at Todo %s." % Todo_id)