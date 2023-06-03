from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "all_tasks_list"
    template_name = "todo/home.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_edit.html"
