from django.contrib import messages
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ("created_at",)

    TASK_STATUS = (
        ("n", "New"),
        ("ip", "In progress"),
        ("com", "Completed"),
        ("can", "Cancelled"),
    )

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=3,
        choices=TASK_STATUS,
        blank=True,
        default="a",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    is_deadline_notification_sent = models.BooleanField(default=False)
    files = models.FileField(upload_to="task_files/", null=True, blank=True)
    assigned_users = models.ManyToManyField(
        User, related_name="assigned_tasks", blank=True
    )
    completed_by = models.ManyToManyField(
        User, related_name="completed_tasks", blank=True
    )
    is_completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    def send_notification(self, request):
        is_deadline_notification_sent = self.is_deadline_notification_sent
        is_deadline = (
            self.end_date
            and self.end_date - timezone.now() <= timezone.timedelta(days=1)
        )

        if not is_deadline_notification_sent and is_deadline:
            messages.add_message(
                request,
                messages.WARNING,
                f'Task "{self.title}" is approaching its deadline!',
            )
            self.is_deadline_notification_sent = True
            self.save()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
