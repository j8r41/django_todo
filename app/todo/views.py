from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import (
    CommentForm,
    TaskAssignedUsersForm,
    TaskCompletionForm,
    TaskForm,
)
from .models import Comment, Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "all_tasks_list"
    template_name = "todo/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_tasks_list"] = context["all_tasks_list"].filter(
            Q(user=self.request.user) | Q(assigned_users=self.request.user)
        )

        for task in context["all_tasks_list"]:
            task.send_notification(self.request)

        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "todo/task_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if (
            self.object.user != request.user
            and request.user not in self.object.assigned_users.all()
        ):
            raise Http404("You are not allowed to view this task.")

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user=request.user, task=task, text=form.cleaned_data["text"]
            )
            return redirect("task_detail", pk=task.pk)
        else:
            comments = task.comments.all()
            context = {
                "task": task,
                "comments": comments,
                "comment_form": form,
            }
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        comments = task.comments.all()
        comment_form = CommentForm()
        task_completion_form = TaskCompletionForm()
        if (
            task.user == self.request.user
            or self.request.user in task.assigned_users.all()
        ) and not task.is_completed:
            context["task_completion_form"] = task_completion_form
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context


class MarkTaskAsCompletedView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return HttpResponseBadRequest()

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskCompletionForm(request.POST)
        if form.is_valid():
            is_completed = form.cleaned_data["is_completed"]
            if is_completed:
                task.is_completed = True
                task.completed_by.add(request.user)
                task.save()
            else:
                task.is_completed = False
                task.completed_by.remove(request.user)
                task.save()
            return redirect("task_detail", pk=task.pk)
        else:
            return HttpResponseBadRequest()


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_new.html"
    success_url = reverse_lazy("home")
    success_message = "Task was created successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_edit.html"
    success_url = reverse_lazy("home")
    success_message = "Task was updated successfully."

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.filter(user=user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
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


class TaskAssignedUsersView(
    LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = Task
    form_class = TaskAssignedUsersForm
    template_name = "todo/task_add_users.html"
    success_url = reverse_lazy("home")
    success_message = "Users were added successfully."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user != request.user:
            raise Http404("You are not allowed to add users to this task.")

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskAssignedUsersView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
