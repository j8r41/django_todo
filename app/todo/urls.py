from django.urls import path

from .views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/new/", TaskCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete",
    ),
]
