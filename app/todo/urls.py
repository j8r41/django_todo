from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/new/", TaskCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
]
