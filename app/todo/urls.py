from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
]
