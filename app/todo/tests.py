from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import pytz

from .models import Task


class TaskTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            password="secret_password",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            password="secret_password",
        )

        self.task = Task.objects.create(
            title="A good title",
            description="A nice description",
            end_date="2023-06-05 11:30:00",
            status="n",
            user=self.user1,
            is_deadline_notification_sent=False,
        )

    def test_string_representation(self):
        task = Task(title="A sample title")
        self.assertEqual(str(task), task.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.task.get_absolute_url(), "/task/1/")

    def test_task_content(self):
        self.assertEqual(f"{self.task.title}", "A good title")
        self.assertEqual(f"{self.task.description}", "A nice description")
        now = timezone.now()
        self.assertLessEqual(self.task.created_at, now)
        self.assertGreaterEqual(
            self.task.created_at, now - timedelta(seconds=1)
        )
        self.assertEqual(f"{self.task.end_date}", "2023-06-05 11:30:00")
        self.assertEqual(f"{self.task.status}", "n")
        self.assertEqual(f"{self.task.user}", "testuser1")
        self.assertFalse(self.task.is_deadline_notification_sent)

    def test_login_required_redirect(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)

    def test_task_list_view(self):
        self.client.login(username="testuser1", password="secret_password")
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("home"))
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "todo/home.html")

    def test_task_detail_view(self):
        self.client.login(username="testuser1", password="secret_password")
        response = self.client.get("/task/1/")
        no_response = self.client.get("/task/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "todo/task_detail.html")

    def test_task_create_view(self):
        self.client.login(username="testuser1", password="secret_password")
        response = self.client.post(
            reverse("task_new"),
            {
                "title": "New title",
                "description": "New text",
                "end_date": "2023-06-05 11:30:00",
                "status": "n",
                "user": self.user1.id,
                "is_deadline_notification_sent": "false",
                "assigned_users": self.user2.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.last().title, "New title")
        self.assertEqual(Task.objects.last().description, "New text")
        self.assertEqual(
            Task.objects.last().end_date,
            datetime(2023, 6, 5, 11, 30, tzinfo=pytz.UTC),
        )
        self.assertEqual(Task.objects.last().status, "n")
        self.assertFalse(Task.objects.last().is_deadline_notification_sent)

    def test_task_update_view(self):
        self.client.login(username="testuser1", password="secret_password")
        response = self.client.post(
            reverse("task_edit", args="1"),
            {
                "title": "Updated title",
                "description": "Updated text",
                "end_date": "2023-06-06 11:40:00",
                "status": "ip",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_task_delete_view(self):
        self.client.login(username="testuser1", password="secret_password")
        response = self.client.post(reverse("task_delete", args="1"))
        self.assertEqual(response.status_code, 302)
