from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def completeTodo(request, id):
    todo = Todo.objects.get(pk=id)
    todo.complete = True
    todo.save()

    return render(request, 'complete.html')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return render(request, 'deletecomplete.html')

def deleteAll(request):
    Todo.objects.all().delete()

    return render(request, 'deleteall.html')
