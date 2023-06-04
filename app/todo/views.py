from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "all_tasks_list"
    template_name = "todo/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_tasks_list"] = context["all_tasks_list"].filter(
            user=self.request.user
        )
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todo/task_detail.html"


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    template_name = "todo/task_new.html"
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Task was created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "todo/task_edit.html"
    fields = "__all__"
    success_url = reverse_lazy("home")
    success_message = "Task was updated successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "todo/task_delete.html"
    success_url = reverse_lazy("home")
    success_message = "Task was deleted successfully."

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response
