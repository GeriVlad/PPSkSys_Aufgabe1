from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.urls import reverse
import datetime

from .models import Todo
from .forms import TodoForm

def index(request):
    latest_todo_list = Todo.objects.order_by('-last_modified')[:5]
    all_todos = Todo.objects.all()
    # context = {'latest_todo_list': latest_todo_list}
    context = {'all_todos': all_todos}
    return render(request, 'todos/html/overview.html', context)

def detail(request, Todo_id):
    return HttpResponse("You're looking at Todo %s." % Todo_id)

def edit(request, Todo_id):
    todo = get_object_or_404(Todo, pk=Todo_id)
   
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            Todo.todo_text = form.clean_todo_deadline_Form['todo_text_Form']
            #Todo.deadline = form.clean_todo_deadline_Form['todo_deadline_Form'] 
            Todo.progress = form.clean_todo_progress_Form['todo_progress_Form']
            Todo.save()

            return HttpResponseRedirect(reverse('todo - saved'))
    else:
        form = TodoForm

        context = {
            'form': form,
            'todo': todo,
        }
        return render(request, 'todos/html/edittodo.html', context)
    # try:
    #     selected_todo = get(pk=request.POST)
    # except (KeyError, Todo.DoesNotExist):
    #     return render(request, 'todo/detail.html', {
    #         'todo': todo,
    #         'error_message': "error... something went wrong",
    #     })
    # else:  
    #     selected_todo.save()
    #     return HttpResponseRedirect(reverse('todo:overview'))


    return render(request, 'todos/html/edittodo.html', {'todo': todo})

def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            Todo.todo_text = form.cleaned_data['todo_text']
            #Todo.deadline = form.cleaned_data['deadline'] 
            Todo.progress = form.cleaned_data['progress']

            Todo.save()

            return HttpResponseRedirect(reverse('todos/html/impressum.html'))
        else:
            
            return HttpResponseRedirect('overview')
    else:
        form = TodoForm

        context = {
            'form': form,
            'todo': Todo,
        }
        return render(request, 'todos/html/newtodo.html', context)

def impressum(request):
    return render(request, 'todos/html/impressum.html')

def delete(request, Todo_id):
    if request.method == 'POST':
        Todo.objects.filter(id=Todo_id).delete()
        return(HttpResponseRedirect(reverse('overview')))
    else:
        return Http404("You're in the wrong place!")