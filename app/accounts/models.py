from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telegram = models.CharField(
        max_length=50, blank=True, null=True, unique=True
    )
