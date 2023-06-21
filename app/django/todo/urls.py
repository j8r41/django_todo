from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.views import TaskListAPIView
from .views import (
    LeaveTaskView,
    MarkTaskAsCompletedView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskInvitationsListView,
    TaskListView,
    TaskPendingUsersView,
    TaskUpdateView,
)

router = DefaultRouter()
# router.register(
#     "tasks/<str:telegram_key>/",
#     TaskListAPIView.as_view(),
#     basename="task-list",
# )

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("", include(router.urls)),
    path(
        "api/v1/task/<str:telegram_key>/",
        TaskListAPIView.as_view(),
        name="task-list",
    ),
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
        "task/<int:pk>/leave/",
        LeaveTaskView.as_view(),
        name="task_leave",
    ),
    path(
        "task/invitations/",
        TaskInvitationsListView.as_view(),
        name="task_invitations",
    ),
]
