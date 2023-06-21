from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from ..models import Task
from .serializers import TaskSerializer

User = get_user_model()


class TaskListAPIView(ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        telegram_key = self.kwargs["telegram_key"]
        if not User.objects.filter(telegram_key=telegram_key).exists():
            raise NotFound(
                f"User with telegram_key={telegram_key} does not exist"
            )
        return Task.objects.filter(user__telegram_key__exact=telegram_key)
