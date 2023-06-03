from django.contrib.auth.models import User
from django.db import models
from todo.models import Task


class UserProfile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("user",)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
