from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from .models import ToDoList, ToDoItem
from .forms import *
from django.urls import reverse


class ToDoList_LV(ListView):
    model = ToDoList
    context_object_name = 'todos'
    paginate_by = 5
    query_set = ToDoList.objects.all().order_by('id').values()
    template_name = "index.html"


class TodoItem_LV(ListView):
    model = ToDoItem
    paginate_by = 8
    template_name = "todolist.html"


    def get_context_data(self):
        context = super().get_context_data()
        context["todo"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["items"] = ToDoItem.objects.filter(todoList_id=self.kwargs["list_id"])
        return context
    
def todo_item_list(request, list_id):
    todo_list = get_object_or_404(ToDoList, pk=list_id)
    todo_items = todo_list.todoitem_set.all()
    return render(request, 'todolist.html', {'todo_list': todo_list, 'todo_items': todo_items})

def list_create(request):
    if request.method == "POST":
        formulario = ToDoListForm(request.POST)
        if formulario.is_valid():
            todo_list = formulario.save(commit=False)
            todo_list.title = formulario.cleaned_data['title']
            todo_list.category = formulario.cleaned_data['category']
            todo_list.created_date = formulario.cleaned_data['created_date']
            todo_list.due_date = formulario.cleaned_data['due_date']
            todo_list.state = formulario.cleaned_data['state']
            todo_list.save()
            return redirect('index')
    else:
        formulario = ToDoListForm()
    return render(request, 'todolist_new.html', {'formulario': formulario})

def list_update(request, pk):
    todo_list = get_object_or_404(ToDoList, pk=pk)
    if request.method == "POST":
        formulario = ToDoListForm(request.POST, instance=todo_list)
        if formulario.is_valid():
            todo_list = formulario.save(commit=False)
            todo_list.title = formulario.cleaned_data['title']
            todo_list.category = formulario.cleaned_data['category']
            todo_list.created_date = formulario.cleaned_data['created_date']
            todo_list.due_date = formulario.cleaned_data['due_date']
            todo_list.state = formulario.cleaned_data['state']
            todo_list.save()
            return redirect('index')
    else:
        formulario = ToDoListForm(instance=todo_list)
    return render(request, 'todolist_new.html', {'formulario': formulario, 'update': 'Si'})

def list_delete(request, pk):
    todo_list = get_object_or_404(ToDoList,pk=pk)
    todo_list.delete()
    return redirect('index')

def item_create(request,list_id):
    todo = get_object_or_404(ToDoList, pk=list_id)
    if request.method == "POST":
        formulario = ToDoItemForm(request.POST)
        if formulario.is_valid():
            item = formulario.save(commit=False)
            item.title = formulario.cleaned_data['title']
            item.description = formulario.cleaned_data['description']
            item.todoList = formulario.cleaned_data['todoList']
            item.save()
        return render(request, 'index.html',{'todo': todo})
    else:
        formulario = ToDoItemForm()
    return render(request, 'todoitem_new.html', {'formulario': formulario, 'todo': todo})

def item_update(request, pk):
    if request.method == "POST":
        formulario = ToDoListForm(request.POST, instance=todo_list)
        if formulario.is_valid():
            todo_list = formulario.save(commit=False)
            todo_list.title = formulario.cleaned_data['title']
            todo_list.description = formulario.cleaned_data['description']
            todo_list.todoList = formulario.cleaned_data['todoList']
            todo_list.save()
            return redirect('index')
    else:
        formulario = ToDoListForm(instance=todo_list)
    return render(request, 'todolist_new.html', {'formulario': formulario, 'update': 'Si'})


def item_delete(request, pk):
    item = get_object_or_404(ToDoItem,pk=pk)
    item.delete()
    return redirect('index')


# https://realpython.com/django-todo-lists/