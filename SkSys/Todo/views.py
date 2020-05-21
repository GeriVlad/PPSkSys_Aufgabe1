from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Todo

def index(request):
    latest_todo_list = Todo.objects.order_by('-last_modified')[:5]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'todos/html/overview.html', context)

def detail(request, Todo_id):
    return HttpResponse("You're looking at Todo %s." % Todo_id)