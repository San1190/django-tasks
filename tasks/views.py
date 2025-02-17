from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse_lazy
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return render(request, "tasks/partials/task_item.html", {"task": task})


@csrf_exempt
def delete_task(request, task_id):
    if request.method == "POST" and request.POST.get("_method") == "DELETE":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return HttpResponse('')  # Devuelve una respuesta vacía para que HTMX lo elimine
    return JsonResponse({"error": "Método no permitido"}, status=405)
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        # Return an empty response with the HX-Trigger header to refresh the task list
    tasks = Task.objects.all()
    return render(request, "tasks/partials/task_list.html", {"tasks": tasks})