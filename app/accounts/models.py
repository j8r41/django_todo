import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telegram_key = models.CharField(
        max_length=30, unique=True, blank=True, null=True
    )
    is_telegram_verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.telegram_key:
            self.telegram_key = secrets.token_hex(10)
        super().save(*args, **kwargs)

    def generate_telegram_key(self):
        self.telegram_key = secrets.token_hex(10)
        self.save()
