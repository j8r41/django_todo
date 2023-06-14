from django.urls import path

from .views import (
    MarkTaskAsCompletedView,
    TaskPendingUsersView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskInvitationsListView,
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
    path(
        "task/<int:pk>/share/",
        TaskPendingUsersView.as_view(),
        name="task_add_users",
    ),
    path(
        "task/<int:pk>/complete/",
        MarkTaskAsCompletedView.as_view(),
        name="mark_task_as_completed",
    ),
    path(
        "task/invitations/",
        TaskInvitationsListView.as_view(),
        name="task_invitations",
    ),
]
