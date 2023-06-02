from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    context = {}
    context["tasks"] = tasks
    return render(request, "todo/index.html", context)
