from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import check_password


class SignupPageTests(TestCase):
    username = "newuser"
    password = "secret"

    def test_signup_page_status_code(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        new_user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertTrue(check_password(self.password, new_user.password))
