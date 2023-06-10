from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import pytz

from .models import Task, Comment


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

        self.task1 = Task.objects.create(
            title="A good title",
            description="A nice description",
            end_date="2023-06-05 11:30:00",
            status="n",
            user=self.user1,
            is_deadline_notification_sent=False,
        )
        self.task2 = Task.objects.create(
            title="A bad title",
            description="A bad description",
            end_date="2023-01-05 23:30:00",
            status="ip",
            user=self.user2,
            is_deadline_notification_sent=False,
        )
        self.task1.assigned_users.add(self.user2)

    def test_string_representation(self):
        task1 = Task(title="A sample title")
        self.assertEqual(str(task1), task1.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.task1.get_absolute_url(), "/task/5/")

    def test_task_content(self):
        self.assertEqual(f"{self.task1.title}", "A good title")
        self.assertEqual(f"{self.task1.description}", "A nice description")
        now = timezone.now()
        self.assertLessEqual(self.task1.created_at, now)
        self.assertGreaterEqual(
            self.task1.created_at, now - timedelta(seconds=1)
        )
        self.assertEqual(f"{self.task1.end_date}", "2023-06-05 11:30:00")
        self.assertEqual(f"{self.task1.status}", "n")
        self.assertEqual(f"{self.task1.user}", "testuser1")
        self.assertFalse(self.task1.is_deadline_notification_sent)

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

    def test_assigned_users(self):
        assigned_users = self.task1.assigned_users.all()
        self.assertEqual(len(assigned_users), 1)
        self.assertIn(self.user2, assigned_users)

    def test_assigned_tasks(self):
        assigned_tasks = self.user2.assigned_tasks.all()
        self.assertEqual(len(assigned_tasks), 1)
        self.assertIn(self.task1, assigned_tasks)


class CommentTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            password="secret_password",
        )
        self.task1 = Task.objects.create(
            title="A good title",
            description="A nice description",
            end_date="2023-06-05 11:30:00",
            status="n",
            user=self.user1,
            is_deadline_notification_sent=False,
        )
        self.comment1 = Comment.objects.create_user(
            user=self.user1,
            task=self.task1,
            text="A good text",
        )

    def test_string_representation(self):
        comment1 = Comment(text="A sample text")
        self.assertEqual(str(comment1), comment1.text)

    def test_task_content(self):
        self.assertEqual(f"{self.comment1.user}", "testuser1")
        self.assertEqual(f"{self.comment1.task}", "A good title")
        self.assertEqual(f"{self.comment1.text}", "A good text")
        
    # TODO: Test CRUD CommentModel 