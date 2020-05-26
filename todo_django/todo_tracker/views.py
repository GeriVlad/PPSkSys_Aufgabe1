from django.shortcuts import render, redirect
# from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import TodoForm

def index(request):
    return render(request, 'todo_tracker/index.html')

def overview(request):
    todos = Todo.objects.all()          

    context = {'todos': todos}
    return render(request, 'todo_tracker/overview.html', context)

def deletetodo(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('overview')

def edittodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('overview')

    context = {'todo': todo, 'form': form}
    return render(request, 'todo_tracker/edittodo.html', context)

def newtodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('overview')

    context = {'form': form}
    return render(request, 'todo_tracker/newtodo.html', context)

def impressum(request):
    return render(request, 'todo_tracker/impressum.html')
