from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return render(request, "tasks/partials/task_item.html", {"task": task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponse("")

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
    tasks = Task.objects.all()
    return render(request, "tasks/partials/task_list.html", {"tasks": tasks})