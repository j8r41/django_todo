from django.db import models
from django.urls import reverse


class Task(models.Model):
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ("title",)

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

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
