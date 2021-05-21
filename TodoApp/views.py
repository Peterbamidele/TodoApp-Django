from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'TodoApp/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    # print(request.POST['text'])

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.complete = True
    todo.save()
    return redirect('index', Todo_id=todo.id)


def deleteCompleted(request, Todo_id=None):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')

# Create your views here.
