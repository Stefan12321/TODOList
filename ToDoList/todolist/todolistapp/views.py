from django.shortcuts import render
from .forms import AddTaskForm
from .models import Task
from django.contrib.auth.models import User


def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            tasks_list = Task.objects.filter(user=request.user.id)
            return render(request, 'todolistapp/index.html', {'tasks_list': tasks_list})
    return render(request, 'todolistapp/index.html')


def add_task(request):
    add_task_form = AddTaskForm()
    if request.method == "POST":
        print(request.POST)
        print(request.user.id)
        task = Task()
        task.description = request.POST.get('task')
        task.user = User.objects.get(id=request.user.id)
        task.time = request.POST.get('deadline')
        task.is_completed = False
        task.save()
    return render(request,'todolistapp/add_task.html',{'form': add_task_form} )