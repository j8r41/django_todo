from django.contrib.auth.models import User
from django.test import TestCase

from .models import Task


class TaskTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="secret_password",
        )

        self.task = Task.objects.create(
            title="A test title",
            description="A test description",
            created_at="2023-06-05 10:30:00",
            end_date="2023-06-05 11:30:00",
            status="n",
            user=self.user,
        )

    def test_string_representation(self):
        task = Task(title="A sample title")
        self.assertEqual(str(task), task.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.task.get_absolute_url(), "/task/1/")
