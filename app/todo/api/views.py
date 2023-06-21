from rest_framework.generics import ListAPIView

from ..models import Task
from .serializers import TaskSerializer


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        telegram_key = self.kwargs["telegram_key"]
        return Task.objects.filter(user__telegram_key__exact=telegram_key)
