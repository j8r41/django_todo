from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages

from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "all_tasks_list"
    template_name = "todo/home.html"


class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/task_detail.html"


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    template_name = "todo/task_new.html"
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Task was created successfully."


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "todo/task_edit.html"
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Task was updated successfully."


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "todo/task_delete.html"
    success_url = reverse_lazy("home")
    success_message = "Task was deleted successfully."

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response
