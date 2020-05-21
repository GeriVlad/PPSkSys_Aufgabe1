from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Todo

def index(request):
    latest_todo_list = Todo.objects.order_by('-last_modified')[:5]
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'todos/html/overview.html', context)

def detail(request, Todo_id):
    return HttpResponse("You're looking at Todo %s." % Todo_id)

def edit(request, Todo_id):
    todo = get_object_or_404(Todo, pk=Todo_id)
   # if request.method == POST

    
    try:
        selected_todo = get(pk=request.POST)
    except (KeyError, Todo.DoesNotExist):
        return render(request, 'todo/detail.html', {
            'todo': todo,
            'error_message': "error... something went wrong",
        })
    else:  
        selected_todo.save()
        return HttpResponseRedirect(reverse('todo:overview'))


    return render(request, 'todos/html/edittodo.html', {'todo': todo})

def new(request):
    return render(request, 'todos/html/newtodo.html')

def impressum(request):
    return render(request, 'todos/html/impressum.html')